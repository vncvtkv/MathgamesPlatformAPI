import { createRouter, createWebHistory } from 'vue-router' // Import createWebHistory
import HomePage from '../components/HomePage.vue'
import AboutPage from '../components/AboutPage.vue'
import PostDetail from '../components/PostDetail.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/about',
    name: 'AboutPage',
    component: AboutPage
  },
  {
    path: '/post/:id',  //  Параметр :id
    name: 'PostDetail',
    component: PostDetail,
    props: true   //  Передаем :id как prop
  }
]

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory
  routes
})

export default router