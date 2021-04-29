import Vue from 'vue'
import { date } from 'quasar'

Vue.filter('currency', value => value && value.toLocaleString('it-IT', { style: 'currency', currency: 'EUR' }))
Vue.filter('currencyInt', value => value && value.toLocaleString('it-IT', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 }))
Vue.filter('datetime', value => value && date.formatDate(value, 'DD/MM/YYYY - HH:mm'))
Vue.filter('date', value => value && date.formatDate(value, 'DD/MM/YYYY'))
