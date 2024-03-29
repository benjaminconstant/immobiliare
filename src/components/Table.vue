<template>
  <q-table
    ref="table"
    dense
    class="bg-grey-5 q-pa-xl"
    hide-bottom
    wrap-cells
    :pagination="pagination"
    :loading="pending"
    separator="cell"
    binary-state-sort
    :data="houses"
    color="secondary"
    :columns="columns"
    row-key="id"
    :filter="filter"
  >
    <template #top>
      <div class="row justify-around fit items-center text-secondary">
        <q-select
          v-model="selectedSearch"
          filled
          color="secondary"
          label="Ricerca"
          :options="searchOptions"
          @input="onSearchChange($event)"
        />
        <q-input
          v-model="filter"
          clearable
          debounce="500"
          color="secondary"
          placeholder="Cerca"
        />
        <h4>
          {{ houseCounter }} Annunci
        </h4>
        <q-btn
          unelevated
          outline
          icon="refresh"
          @click="$store.dispatch('getHouses')"
        />
        <span>ultimo aggiornamento: {{ lastUpdate }}</span>
        <q-toggle
          v-model="isHidden"
          color="secondary"
          :label="isHidden ? 'Nascoste' : 'Visibili'"
        />
      </div>
      <div class="row q-pb-lg items-center fit text-secondary q-gutter-md">
        <div class="col q-gutter-md">
          <FilterInput field-name="price_min" field-label="Prezzo MIN" />
          <FilterInput field-name="price_max" field-label="Prezzo MAX" />
        </div>
        <div class="col q-gutter-md">
          <FilterInput field-name="price_mq_min" field-label="Prezzo MQ MIN" />
          <FilterInput field-name="price_mq_max" field-label="Prezzo MQ MAX" />
        </div>
        <div class="col q-gutter-md">
          <FilterInput field-name="mq_min" field-label="MQ MIN" />
          <FilterInput field-name="mq_max" field-label="MQ MAX" />
        </div>
        <div v-if="selectedSearch.platform !=2" class="col q-gutter-md">
          <FilterInput field-name="costs_min" field-label="Spese MIN" />
          <FilterInput field-name="costs_max" field-label="Spese MAX" />
        </div>
        <div v-if="selectedSearch.platform !=2" class="col q-gutter-md">
          <FilterSelect field-name="state" field-label="Stato" />
        </div>
      </div>
    </template>
    <template #body-cell-link="props">
      <q-td class="text-center">
        <q-btn
          class="text-bold text-white"
          no-caps
          type="a"
          color="secondary"
          target="_blank"
          :href="props.row.link"
          label="Link"
        />
      </q-td>
    </template>
    <template #body-cell-created="props">
      <q-td class="text-center">
        <span :class="date.isSameDate(props.row.created, new Date(), 'day') ? 'text-warning' : ''">{{ date.formatDate(props.row.created, 'DD-MM-YYYY') }}</span>
      </q-td>
    </template>
    <template #body-cell-title="props">
      <q-td
        :class="{'bg-red' : !props.row.has_changed}"
        class="text-center"
        style="max-width: 400px"
      >
        {{ props.row.title }}
        <q-tooltip
          content-class="bg-dark"
          content-style="font-size: 20px"
          max-width="50vw"
        >
          {{ props.row.text }}
        </q-tooltip>
        <q-icon
          v-if="!props.row.has_changed"
          size="lg"
          color="negative"
          name="delete"
          @click="$store.dispatch('deleteHouse', props.row)"
        />
      </q-td>
    </template>
    <template #body-cell-is_interesting="props">
      <q-td class="text-center">
        <div>
          <q-icon
            size="lg"
            :color="props.row.is_interesting ? 'warning' : 'grey'"
            name="star"
            @click="$store.dispatch('putInteresting', props.row)"
          />
          <q-icon
            size="lg"
            :color="props.row.is_hidden ? 'positive' : 'negative'"
            :name="props.row.is_hidden ? 'restore' : 'delete'"
            @click="$store.dispatch('putHidden', props.row)"
          />
        </div>
      </q-td>
    </template>
    <template #body-cell-price_mq="props">
      <q-td class="text-center">
        <span :class="price_mqColor(props.row.price_mq)">
          {{ props.row.price_mq | currency }}
        </span>
      </q-td>
    </template>
    <template #body-cell-costs="props">
      <q-td class="text-center">
        <span :class="costsColor(props.row.costs)">
          {{ formatCurrency(props.row.costs) }}
        </span>
      </q-td>
    </template>
    <template #body-cell-is_private="props">
      <q-td class="text-center" :class="props.row.is_private && 'bg-positive'">
        <div style="width: 20vw" class="row">
          <q-intersection
            v-for="img in props.row.image_set"
            :key="img.url"
            once
            transition="scale"
            class="col q-mx-xs"
          >
            <q-img :src="img.url">
              <q-tooltip>
                <q-img style="width: 30vw" :src="img.url" />
              </q-tooltip>
            </q-img>
          </q-intersection>
        </div>
      </q-td>
    </template>
    <template #body-cell-note="props">
      <q-td class="text-center">
        <q-input
          autogrow
          :value="props.row.note"
          type="textarea"
          debounce="500"
          @input="onNoteChange(props.row, $event)"
        />
      </q-td>
    </template>
  </q-table>
</template>

<script>
import FilterInput from 'components/FilterInput'
import FilterSelect from 'components/FilterSelect'
import { mapGetters, mapMutations, mapState } from 'vuex'
import { date } from 'quasar'
export default {
  name: 'Table',
  components: { FilterInput, FilterSelect },
  data () {
    return {
      date,
      selectedSearch: '',
      isHidden: false,
      filter: '',
      pagination: {
        sortBy: 'created',
        descending: true,
        rowsPerPage: 0
      },
      columns: [
        {
          name: 'date_publish',
          label: 'Data',
          align: 'left',
          field: row => row.date_publish,
          format: val => date.formatDate(val, 'DD-MM-YYYY'),
          sortable: true,
          style: 'min-width: 110px'
        },
        {
          name: 'created',
          label: 'Creato',
          align: 'left',
          field: row => row.created,
          format: val => date.formatDate(val, 'DD-MM-YYYY'),
          sortable: true,
          style: 'min-width: 110px'
        },
        {
          name: 'title',
          label: 'Titolo',
          align: 'left',
          field: row => row.has_changed,
          sortable: true
        },
        {
          name: 'is_private',
          label: 'Galleria',
          align: 'left',
          field: row => row.is_private,
          sortable: true
        },
        {
          name: 'costs',
          label: 'Spese',
          align: 'left',
          field: row => row.costs,
          format: val => this.formatCurrency(val),
          sortable: true
        },
        {
          name: 'mq',
          label: 'MQ',
          align: 'left',
          field: row => row.mq,
          sortable: true
        },
        {
          name: 'price_mq',
          label: 'Prezzo MQ',
          align: 'left',
          field: row => row.price_mq,
          format: val => this.formatCurrency(val),
          sortable: true
        },
        {
          name: 'price',
          label: 'Prezzo',
          align: 'left',
          field: row => row.price,
          format: val => this.formatCurrency(val),
          sortable: true
        },
        {
          name: 'link',
          label: 'Link',
          align: 'left',
          field: row => row.link
        },
        // definita per poter utilizzare ricerca, non visibile
        {
          name: 'titleSearch',
          headerStyle: 'display: none',
          style: 'display: none',
          label: 'Titolo',
          align: 'left',
          field: row => row.title
        },
        // definita per poter utilizzare ricerca, non visibile
        {
          name: 'textSearch',
          headerStyle: 'display: none',
          style: 'display: none',
          label: 'Descrizione',
          align: 'left',
          field: row => row.text
        },
        {
          name: 'is_interesting',
          label: '',
          align: 'left',
          field: row => row.is_interesting,
          sortable: true
        },
        {
          name: 'note',
          label: 'Note',
          align: 'left',
          field: row => row.note,
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapGetters(['housesHidden, housesVisible']),
    ...mapState(['pending']),
    searchOptions () {
      return this.$store.state.searches.map(search => ({ label: search.name, value: search.id, platform: search.platform }))
    },
    houses () {
      return this.isHidden ? this.$store.getters.housesHidden : this.$store.getters.housesVisible
    },
    lastUpdate () {
      return date.formatDate(new Date(Math.max(...this.houses.map(h => new Date(h.updated)))), 'DD/MM/YYYY - HH:mm')
    },
    houseCounter () {
      return this.filter ? this.$refs.table.filteredSortedRowsNumber : this.houses.length
    }
  },
  watch: {
    selectedSearch: function (val) {
      if (val === 2) {
        this.updateFilter({ key: 'state', value: null })
        this.updateFilter({ key: 'costs_min', value: null })
        this.updateFilter({ key: 'costs_max', value: null })
      }
    }
  },
  mounted () {
    this.$store.dispatch('getSearches').then(() => {
      this.selectedSearch = this.searchOptions[0]
      this.updateFilter({ key: 'search', value: this.selectedSearch.value })
      this.$store.dispatch('getHouses')
    })
  },
  methods: {
    ...mapMutations(['updateFilter']),
    onSearchChange (value) {
      this.updateFilter({ key: 'search', value: value.value })
      this.$store.dispatch('getHouses')
    },
    onNoteChange (house, note) {
      house.note = note
      this.$store.dispatch('putNote', house)
    },
    formatCurrency (val) {
      return val !== null ? val.toLocaleString('it-IT', { style: 'currency', currency: 'EUR' }) : 'N.D.'
    },
    price_mqColor (value) {
      if (value < 500) {
        return 'text-green-10'
      }
      if (value < 1000) {
        return 'text-green-5'
      }
      if (value < 1250) {
        return 'text-yellow'
      }
      if (value < 1500) {
        return 'text-red'
      }
      if (value >= 1500) {
        return 'text-deep-purple-14'
      }
    },
    costsColor (value) {
      if (value < 0) {
        return 'text-black'
      }
      if (value < 25) {
        return 'text-green-10'
      }
      if (value < 50) {
        return 'text-green-5'
      }
      if (value < 75) {
        return 'text-yellow'
      }
      if (value < 100) {
        return 'text-red'
      }
      if (value >= 100) {
        return 'text-deep-purple-14'
      }
    }
  }
}
</script>
<style>
td {
  font-size: 16px !important;
}
th {
  font-size: 22px !important;
}
</style>
