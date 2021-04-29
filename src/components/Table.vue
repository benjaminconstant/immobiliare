<template>
  <q-table
    dense
    class="bg-grey-5 q-pa-xl"
    hide-bottom
    wrap-cells
    :pagination="pagination"
    binary-state-sort
    :data="houses"
    :columns="columns"
    row-key="id"
    :filter="filter"
  >
    <template #top>
      <div class="row justify-around fit items-center text-secondary">
        <q-input
          v-model="filter"
          clearable
          color="secondary"
          placeholder="Cerca"
        />
        <h4>
          {{ houses.length }} Annunci
        </h4>
        <span>ultimo aggiornamento: {{ lastUpdate }}</span>
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
  </q-table>
</template>

<script>
import FilterInput from 'components/FilterInput'
import { mapState } from 'vuex'
import { date } from 'quasar'
export default {
  name: 'Table',
  components: { FilterInput },
  data () {
    return {
      filter: '',
      pagination: {
        sortBy: 'date_publish',
        descending: true,
        rowsPerPage: 0
      },
      columns: [
        {
          name: 'date_publish',
          label: 'Pubblicato',
          align: 'left',
          field: row => row.date_publish,
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
          field: row => row.link,
          sortable: true
        },
        // definita per poter utilizzare ricerca, non visibile
        {
          name: 'text',
          headerStyle: 'display: none',
          style: 'display: none',
          label: 'Descrizione',
          align: 'left',
          field: row => row.text,
          sortable: true
        },
        {
          name: 'is_interesting',
          label: '',
          align: 'left',
          field: row => row.is_interesting,
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapState(['houses']),
    lastUpdate () {
      return date.formatDate(new Date(Math.max(...this.houses.map(h => new Date(h.updated)))), 'DD/MM/YYYY - HH:mm')
    }
  },
  mounted () {
    this.$store.dispatch('getHouses')
    setInterval(() => this.$store.dispatch('getHouses'), 10000)
  },
  methods: {
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
