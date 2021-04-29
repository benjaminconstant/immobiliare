import { api } from 'boot/axios'
import Vuex from 'vuex'
import Vue from 'vue'

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
    filters: {
      price_min: 0,
      price_max: 0,
      price_mq_min: 0,
      price_mq_max: 0,
      mq_min: 0,
      mq_max: 0,
      costs_min: 0,
      costs_max: 0
    }
  },
  mutations: {
    SET_HOUSES (state, data) {
      state.houses = data
    },
    updateFilter (state, { key, value }) {
      state.filters[key] = value
    }
  },
  actions: {
    getHouses ({ commit, getters }) {
      api.get('houses/' + getters.queryParams).then(r => commit('SET_HOUSES', r.data))
    },
    putInteresting ({ commit }, house) {
      house.is_interesting = !house.is_interesting
      api.put('houses/' + house.id + '/', house)
    }
  },
  getters: {
    queryParams: function (state) {
      let queryString = ''
      Object.keys(state.filters).forEach(key => {
        if (state.filters[key]) {
          queryString += '&' + key + '=' + state.filters[key]
        }
      })
      return queryString.replace('&', '?')
      // return Object.keys(state.filters).map(key => key + '=' + state.filters[key]).join('&');
    }
  }
})

export default Store
