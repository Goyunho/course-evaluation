import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Main from '../views/Main'
import PageNotFound from '../views/PageNotFound'
import University from '../views/University'
import Undergraduate from '../views/Undergraduate'
import Department from '../views/Department'
import Faculty from '../views/Faculty'
import Course from '../views/Course'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/index',
      name: 'index',
      component: Main,
      children: [
        {
          path: '',
          redirect: {name:'home'}
        },
        {
          path: 'univ',
          name: 'university',
          components: {
            main: University
          }
        },
        {
          path: 'under',
          name: 'undergraduate',
          components: {
            main: Undergraduate
          }
        },
        {
          path: 'depart',
          name: 'department',
          components: {
            main: Department
          }
        },
        {
          path: 'faculty',
          name: 'faculty',
          components: {
            main: Faculty
          }
        },
        {
          path: 'course',
          name: 'course',
          components: {
            main: Course
          }
        }
      ]
    },
    {
      path: '*',
      name: 'pagenotfound',
      component: PageNotFound
    }
  ]
})
