<template>
  <div id="app">
  
    <nav>
      <router-link to="/">Main |</router-link> 
      <router-link to="/about"> About us |</router-link> 
      <router-link v-if="isAuthenticated" to="/post/create"> Create New Post |</router-link> 
      <router-link v-if="!isAuthenticated" to="/register">Register</router-link>
      <span v-if="isAuthenticated" class="user-info">
    <div>Welcome, {{ username }}!   <button @click="logout" class="logout-btn">Logout</button></div>
    </span>
    </nav>
    <router-view/>
  </div>
</template>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none; /* Убираем подчеркивание */
}

.user-info {
  display: block;
  margin-left: 10px;
  margin-top: 5px;
}

.user-info button {
  margin-top: 5px;
}
</style>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      username: 'Guest',
      isAuthenticated: false
    }
  },
  created() {
    this.checkAuthStatus();
    this.$router.afterEach(this.checkAuthStatus);
  },
  methods: {
    async checkAuthStatus() {
      const token = localStorage.getItem('access_token');
      this.isAuthenticated = !!token;
      
      if (this.isAuthenticated) {
        await this.fetchUserData();
      } else {
        this.username = 'Guest';
      }
    },
    async fetchUserData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
          }
        });
        this.username = response.data.username || response.data.email;
      } catch (error) {
        console.error('Failed to fetch user data:', error);
        this.username = 'User';
      }
    },
    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      this.isAuthenticated = false;
      this.username = 'Guest';
      this.$router.push('/login');
    }
  }
}
</script>
