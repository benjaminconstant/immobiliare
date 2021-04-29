<template>
  <q-input
    clearable
    filled
    color="secondary"
    :label="fieldLabel"
    :value="filters[fieldName]"
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

    }
  },
  computed: { ...mapState(['filters']) },
  methods: {
    ...mapMutations(['updateFilter']),
    onFilterChange (value) {
      this.updateFilter({ key: this.fieldName, value: value })
      this.$store.dispatch('getHouses')
    }
  }
}
</script>
