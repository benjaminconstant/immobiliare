import { api } from 'boot/axios'
import Vuex from 'vuex'
import Vue from 'vue'
import { Notify } from 'quasar'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

const Store = new Vuex.Store({
  state: {
    pending: false,
    houses: [],
    searches: [],
    filters: {
      searches: null,
      price_min: 0,
      price_max: 0,
      price_mq_min: 0,
      price_mq_max: 0,
      mq_min: 0,
      mq_max: 0,
      costs_min: 0,
      costs_max: 0,
      state: null
    }
  },
  mutations: {
    SET_HOUSES (state, data) {
      state.houses = data
    },
    SET_SEARCHES (state, data) {
      state.searches = data
    },
    SET_PENDING (state, data) {
      state.pending = data
    },
    updateFilter (state, { key, value }) {
      state.filters[key] = value
    }
  },
  actions: {
    getHouses ({ commit, getters }) {
      commit('SET_PENDING', true)
      api.get('houses/' + getters.queryParams).then(r => {
        commit('SET_HOUSES', r.data)
        commit('SET_PENDING', false)
      })
    },
    getSearches ({ commit, getters }) {
      return api.get('searches/').then(r => commit('SET_SEARCHES', r.data))
    },
    putInteresting ({ commit }, house) {
      house.is_interesting = !house.is_interesting
      api.put('houses/' + house.id + '/', house)
    },
    putHidden ({ commit }, house) {
      house.is_hidden = !house.is_hidden
      api.put('houses/' + house.id + '/', house)
      Notify.create({
        message: (house.is_hidden ? 'Nascosta: ' : 'Ripristinata: ') + house.title,
        color: house.is_hidden ? 'negative' : 'positive'
      })
    }
  },
  getters: {
    queryParams: state => {
      let queryString = ''
      Object.keys(state.filters).forEach(key => {
        if (state.filters[key]) {
          queryString += '&' + key + '=' + state.filters[key]
        }
      })
      return queryString.replace('&', '?')
      // return Object.keys(state.filters).map(key => key + '=' + state.filters[key]).join('&');
    },
    housesVisible: state => {
      return state.houses.filter(h => !h.is_hidden)
    },
    housesHidden: state => {
      return state.houses.filter(h => h.is_hidden)
    }
  }
})

export default Store
