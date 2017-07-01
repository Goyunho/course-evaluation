import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import univ from '@/components/univ'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/:univ',
      name: 'univ',
      component: univ
    }
  ]
})
