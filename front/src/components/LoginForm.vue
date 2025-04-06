<template>
  <div class="login-form">
    <h2>Login</h2>
    <div v-if="error" class="error-message">{{ error }}</div>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null
    };
  },
  methods: {
    async login() {
      this.error = null;
      try {
        // URL получения токена из Djoser (замените!)
        const response = await axios.post('http://localhost:8000/auth/jwt/create/', {
          username: this.username,
          password: this.password
        });

        // Сохраняем токен (access и refresh)
        const { access, refresh } = response.data;
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        // Перенаправляем на главную страницу (или куда вам нужно)
        this.$router.push('/');
      } catch (error) {
        this.error = error.response?.data || 'Login failed';
      }
    }
  }
};
</script>