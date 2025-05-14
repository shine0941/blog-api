import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Articles from '../views/Articles.vue'
import CreateArticle from '../views/CreateArticle.vue'

const routes = [
  { path: '/', component: Articles },
  { path: '/login', component: Login },
  { path: '/createarticle', component: CreateArticle },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
