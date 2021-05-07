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
          color="secondary"
          placeholder="Cerca"
        />
        <h4>
          {{ houseCounter }} Annunci
        </h4>
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
        <div class="col q-gutter-md">
          <FilterInput field-name="costs_min" field-label="Spese MIN" />
          <FilterInput field-name="costs_max" field-label="Spese MAX" />
        </div>
        <div class="col q-gutter-md">
          <FilterSelect field-name="state" field-label="Stato" />
        </div>
      </div>
    </template>
    <template #body-cell-link="props">
      <q-td>
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
    <template #body-cell-title="props">
      <q-td style="max-width: 400px">
        {{ props.row.title }}
        <q-tooltip
          content-class="bg-dark"
          content-style="font-size: 20px"
          max-width="50vw"
        >
          {{ props.row.text }}
        </q-tooltip>
      </q-td>
    </template>
    <template #body-cell-is_interesting="props">
      <q-td>
        <q-icon
          :color="props.row.is_interesting ? 'warning' : 'grey'"
          name="star"
          size="lg"
          @click="$store.dispatch('putInteresting', props.row)"
        />
      </q-td>
    </template>
    <template #body-cell-price_mq="props">
      <q-td>
        <span :class="price_mqColor(props.row.price_mq)">
          {{ props.row.price_mq.toFixed(2) }}
        </span>
      </q-td>
    </template>
    <template #body-cell-costs="props">
      <q-td>
        <span :class="costsColor(props.row.costs)">
          {{ formatCurrency(props.row.costs) }}
        </span>
      </q-td>
    </template>
    <template #body-cell-is_hidden="props">
      <q-td>
        <q-btn
          :label="isHidden ? 'Ripristina' : 'Nascondi'"
          :color="isHidden ? 'positive' : 'negative'"
          @click="$store.dispatch('putHidden', props.row)"
        />
      </q-td>
    </template>
    <template #body-cell-image_set="props">
      <q-td style="width: 20vw">
        <div class="row">
          <q-intersection
            v-for="img in props.row.image_set"
            :key="img.url"
            once
            transition="scale"
            margin="-100px"
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
          label: 'Pubblicato',
          align: 'left',
          field: row => row.date_publish,
          format: val => date.formatDate(val, 'DD-MM-YYYY'),
          sortable: true
        },
        {
          name: 'created',
          label: 'Creato',
          align: 'left',
          field: row => row.created,
          format: val => date.formatDate(val, 'DD-MM-YYYY'),
          sortable: true
        },
        {
          name: 'title',
          label: 'Titolo',
          align: 'left',
          field: row => row.title,
          sortable: true
        },
        {
          name: 'image_set',
          label: 'Galleria',
          align: 'left',
          field: row => row.image_set
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
          name: 'text',
          headerStyle: 'display: none',
          style: 'display: none',
          label: 'Descrizione',
          align: 'left',
          field: row => row.text
        },
        {
          name: 'is_hidden',
          label: '',
          align: 'left',
          field: row => row.is_interesting
        },
        {
          name: 'is_interesting',
          label: '',
          align: 'left',
          field: row => row.is_interesting
        }
      ]
    }
  },
  computed: {
    ...mapGetters(['housesHidden, housesVisible']),
    ...mapState(['pending']),
    searchOptions () {
      return this.$store.state.searches.map(search => ({ label: search.name, value: search.id }))
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
  mounted () {
    this.$store.dispatch('getSearches').then(() => {
      this.selectedSearch = this.searchOptions[0]
      this.updateFilter({ key: 'search', value: this.selectedSearch.value })
      this.$store.dispatch('getHouses')
    })
    setInterval(() => this.$store.dispatch('getHouses'), 10000)
  },
  methods: {
    ...mapMutations(['updateFilter']),
    onSearchChange (value) {
      this.updateFilter({ key: 'search', value: value.value })
      this.$store.dispatch('getHouses')
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
  font-size: 18px !important;
}
th {
  font-size: 24px !important;
}
</style>
