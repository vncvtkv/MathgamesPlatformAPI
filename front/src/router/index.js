import { createRouter, createWebHistory } from 'vue-router' // Import createWebHistory
import HomePage from '../components/HomePage.vue'
import AboutPage from '../components/AboutPage.vue'
import RegisterForm from '../components/RegisterForm.vue'
import LoginForm from '../components/LoginForm.vue'
import PostDetail from '../components/PostDetail.vue'
import CreatePost from '../components/CreatePost.vue';


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
  },
  {
    path: '/register',
    name: 'RegisterForm',
    component: RegisterForm
  },
  {
    path: '/login',
    name: 'LoginForm',
    component: LoginForm
  },
  {
    path: '/post/create',
    name: 'CreatePost',
    component: CreatePost,
    meta: { requiresAuth: true } // Защитите маршрут (требуется аутентификация)
  }
]

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    const isAuthenticated = localStorage.getItem('access_token'); // Проверяем наличие токена
    if (!isAuthenticated) {
      next('/login'); // Перенаправляем на страницу входа
    } else {
      next(); // Разрешаем переход на страницу
    }
  } else {
    next(); // Разрешаем переход на страницу (для неавторизованных маршрутов)
  }
});

export default router