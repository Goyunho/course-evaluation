import axios from 'axios'

import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Vue from 'vue'
import { sync } from 'vuex-router-sync'
import App from './components/App'
import router from './router'
import store from './store'

import global from './global'

Vue.prototype.$http = axios
Vue.prototype.$glob = global

Vue.use(BootstrapVue)

sync(store, router)

const app = new Vue({
  router,
  store,
  ...App
})

export { app, router, store }
