import Vue from 'vue'
import axios from 'axios'

export const api = axios.create({
  baseURL: process.env.DEV ? 'http://localhost:8000/api/' : 'https://invernizzibackend.pythonanywhere.com/api/',
  timeout: 10000
  // headers: {'X-Custom-Header': 'foobar'}
})
Vue.prototype.$axios = api
