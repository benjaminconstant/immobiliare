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
    :filter-method="filterFn"
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
          sortable: true
        },
        {
          name: 'price',
          label: 'Prezzo',
          align: 'left',
          field: row => row.price,
          sortable: true
        },
        {
          name: 'link',
          label: 'Link',
          align: 'left',
          field: row => row.link,
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapState(['houses']),
    lastUpdate () {
      return date.formatDate(this.houses[0]?.updated, 'DD/MM/YYYY - HH:mm')
    }
  },
  mounted () {
    this.$store.dispatch('getHouses')
  },
  methods: {
    filterFn (data, string) {
      // funzione per cercare in tutto l'oggetto
      const results = []
      for (const house of this.houses) {
        for (const val of Object.values(house)) {
          if (val.toString().toLowerCase().includes(string.toLowerCase())) {
            results.push(house)
            break
          }
        }
      }
      return results
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
