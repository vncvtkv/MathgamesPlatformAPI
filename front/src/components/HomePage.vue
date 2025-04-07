<template>
  <div class="home-page">
    <h1>Math Games Blog</h1>
    <div v-if="loading">Loading posts...</div>
    <div v-else-if="error">Error loading posts: {{ error }}</div>
    <div v-else class="post-grid">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <h2 class="post-title">{{ post.title }}</h2>
        <p class="post-excerpt">{{ truncatedText(post.text) }}</p>  <!-- Используем вычисляемое свойство -->
        <p class="post-author">Author: {{ post.author }}</p> <!-- Выводим автора -->
        <router-link :to="`/post/${post.id}`" class="read-more-link">Read More</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
  data() {
    return {
      posts: [],
      loading: false,
      error: null
    };
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('http://localhost:8000/api/blog/post/');
        this.posts = response.data;
      } catch (error) {
        this.error = error.message || 'Failed to load posts';
      } finally {
        this.loading = false;
      }
    },
    truncatedText(text) {
      if (!text) return ''; // Обработка случая, если текста нет
      return text.length > 20 ? text.substring(0, 20) + '...' : text; // Обрезаем текст
    }
  }
};
</script>

<style scoped>
.home-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Адаптивная сетка */
  gap: 20px;
}

.post-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.post-title {
  font-size: 1.3em;
  margin-bottom: 10px;
}

.post-excerpt {
  font-size: 1em;
  color: #555;
}

.read-more-link {
  color: #007bff;
  text-decoration: none;
}

.read-more-link:hover {
  text-decoration: underline;
}
</style>