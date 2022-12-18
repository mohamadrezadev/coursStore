import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue';
import Panel from '../views/Panel.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Courss from '../views/Courss.vue';
import Blog from '../views/Blog.vue';
import About from '../views/About.vue';
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
      path: '/blogs',
      name: 'Blogs',
      component:Blog
    },
    {
      path: '/Courss',
      name: 'courss',
      component:Courss
    },
    {
      path: '/login',
      name: 'login',
      component:Login
    },
    {
      path: '/register',
      name: 'register',
      component:Register
    },
    {
      path: '/Panel',
      name: 'Panel',
      component:Panel
    },
    {
      path: '/about',
      name: 'about',
      component:About

    }
  ]
})

export default router
