import Vue from 'vue'
import axios from 'axios'

export const api = axios.create({
  baseURL: process.env.DEV ? 'http://localhost:8000/api/' : 'https://immobiliare.pythonanywhere.com/api/'
  // headers: {'X-Custom-Header': 'foobar'}
})
Vue.prototype.$axios = api
