<template>
  <q-page class="flex flex-center">
    <div class="q-pa-xl">
      <Table />
    </div>
  </q-page>
</template>

<script>
import Table from 'components/Table'

export default {
  name: 'Index',
  components: { Table }
}
</script>
