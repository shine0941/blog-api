import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Articles from '../views/Articles.vue'

const routes = [
  { path: '/', component: Articles },
  { path: '/login', component: Login },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router