import axios from 'axios';

// Создаем экземпляр axios с базовыми настройками
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/blog/', // Ваш базовый URL API
});

// Добавляем интерсептор для автоматической вставки токена
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Интерсептор для обработки ошибок
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Перенаправляем на страницу входа при 401 ошибке
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;