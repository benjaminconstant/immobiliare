import Vue from 'vue'
import axios from 'axios'
import { Cookies } from 'quasar'

const token = Cookies.get('csrftoken')

export const api = axios.create({
  baseURL: process.env.DEV ? 'http://localhost:8000/api/' : 'https://immobiliare.pythonanywhere.com/api/',
  headers: { 'X-CSRFToken': token }
})
Vue.prototype.$axios = api
