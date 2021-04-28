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
import { date } from 'quasar'
export default {
  name: 'Table',
  data () {
    return {
      filter: '',
      houses: [],
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
    lastUpdate () {
      return date.formatDate(this.houses[0]?.updated, 'DD/MM/YYYY - HH:mm')
    }
  },
  mounted () {
    this.$axios.get('houses/').then(r => (this.houses = r.data))
  },
  methods: {
    filterFn (data, string) {
      // funzione per cercare i tutto l'oggetto
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
