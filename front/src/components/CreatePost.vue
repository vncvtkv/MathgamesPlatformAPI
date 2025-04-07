<template>
  <div class="create-post-form">
    <h2>Create New Post</h2>
    <div v-if="error" class="error-message">{{ error }}</div>
    <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
    <form @submit.prevent="createPost">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="title" required>
      </div>
      <div class="form-group">
        <label for="content">Text:</label>
        <textarea id="content" v-model="text" required rows="5"></textarea>
      </div>
      <button type="submit" :disabled="isLoading">
        {{ isLoading ? 'Creating...' : 'Create Post' }}
      </button>
    </form>
  </div>
</template>

<script>
import axiosInstance from '../axios';

export default {
  name: 'CreatePost',
  data() {
    return {
      title: '',
      content: '',
      error: null,
      successMessage: '',
      isLoading: false
    };
  },
  methods: {
    async createPost() {
      this.error = null;
      this.isLoading = true;
      
      try {
        await axiosInstance.post('post/', {
          title: this.title,
          text: this.text
        });

        this.successMessage = 'Post created successfully!';
        this.title = '';
        this.content = '';
        
        setTimeout(() => {
          this.successMessage = '';
          this.$router.push('/');
        }, 3000);
      } catch (error) {
        this.error = error.response?.data || 'Failed to create post';
        if (error.response?.status === 401) {
          this.error = 'Please login to create posts';
          this.$router.push('/login');
        }
      } finally {
        this.isLoading = false;
      }
    }
  }
};
</script>

<style scoped>
.create-post-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

textarea {
  min-height: 150px;
  resize: vertical;
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff4444;
  margin-bottom: 15px;
  padding: 10px;
  background-color: #ffebee;
  border-radius: 4px;
}

.success-message {
  color: #00C851;
  margin-bottom: 15px;
  padding: 10px;
  background-color: #e8f5e9;
  border-radius: 4px;
}
</style>