import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import bu from '@/components/school/bu'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/bu',
      name: 'bu',
      component: bu
    }
  ]
})
