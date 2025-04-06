import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App) // Создаем экземпляр Vue-приложения

app.use(router)
app.mount('#app')
