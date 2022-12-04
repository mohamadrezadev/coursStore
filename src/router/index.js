import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue';
import Panel from '../views/Panel.vue';
import Login from '../views/Login.vue';
;
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component:Home
    },
    {
      path: '/login',
      name: 'login',
      component:Login
    },
    {
      path: '/Panel',
      name: 'Panel',
      component:Panel
    },
    {
      path: '/about',
      name: 'about',

    }
  ]
})

export default router
