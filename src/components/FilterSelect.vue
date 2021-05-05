<template>
  <q-select
    v-model="value"
    filled
    color="secondary"
    :label="fieldLabel"
    :options="options"
    debounce="500"
    @input="onFilterChange($event)"
  />
</template>

<script>
import { mapMutations, mapState } from 'vuex'

export default {
  name: 'FilterInput',
  props: {
    fieldName: {
      type: String,
      default: String
    },
    fieldLabel: {
      type: String,
      default: String
    }
  },
  data () {
    return {
      value: { label: 'Tutti', value: 0 },
      options: [
        { label: 'Tutti', value: 0 },
        { label: 'Da Ristrutturare', value: 1 },
        { label: 'Buono / Abitabile', value: 2 },
        { label: 'Ottimo / Ristrutturato', value: 3 },
        { label: 'Nuovo / In costruzione', value: 4 },
        { label: 'N.D.', value: 5 }]
    }
  },
  computed: { ...mapState(['filters']) },
  methods: {
    ...mapMutations(['updateFilter']),
    onFilterChange (value) {
      this.updateFilter({ key: this.fieldName, value: value.value })
      this.$store.dispatch('getHouses')
    }
  }
}
</script>
