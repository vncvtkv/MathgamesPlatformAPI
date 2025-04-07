<template>
  <div class="post-detail">
    <div v-if="loading">Loading post...</div>
    <div v-else-if="error">Error loading post: {{ error }}</div>
    <div v-else-if="post">  <!-- Проверяем, что post не null -->
      <h1 class="post-title">{{ post.title }}</h1>
      <p class="post-author">Author: {{ post.author }}</p>
      <p class="post-content">{{ post.text }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PostDetail',
  props: {
    id: {  // Получаем id из router props
      type: [String, Number], //id может быть строкой или числом
      required: true
    }
  },
  data() {
    return {
      post: null,
      loading: false,
      error: null
    };
  },
  mounted() {
    this.fetchPost();
  },
  methods: {
    async fetchPost() {
      this.loading = true;
      this.error = null;
      try {
        const postId = this.$route.params.id; 
        const response = await axios.get(`http://localhost:8000/api/blog/post/${postId}/`);  //  Замените на ваш URL
        this.post = response.data;
      } catch (error) {
        this.error = error.message || 'Failed to load post';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.post-detail {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.post-title {
  font-size: 2em;
  margin-bottom: 10px;
}

.post-author {
  font-size: 1.1em;
  color: #777;
  margin-bottom: 20px;
}

.post-content {
  font-size: 1.2em;
  line-height: 1.6;
}
</style>