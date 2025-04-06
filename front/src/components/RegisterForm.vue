<template>
  <div class="register-form">
    <h2>Register</h2>
    <div v-if="error" class="error-message">{{ error }}</div>
    <form @submit.prevent="register">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      error: null
    };
  },
  methods: {
    async register() {
      this.error = null;
      try {
        // Убрали ненужную переменную response, так как она не используется
        await axios.post('http://localhost:8000/auth/users/', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        // Исправленная строка - правильный метод роутера
        this.$router.push('/login');
      } catch (error) {
        this.error = error.response?.data || 'Registration failed';
      }
    }
  }
};
</script>

<style scoped>
/* Ваши стили */
</style>