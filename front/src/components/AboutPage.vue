<template>
 <div class="about-page">
    <h1>About Us</h1>

    <p class="about-description">Welcome to <b style="font-weight: bold;">Mathgame platform</b>  - a blog and platform dedicated to engaging math games! We believe that mathematics can be interesting and accessible to everyone, and our goal is to share the best games, puzzles, and educational materials that will help you fall in love with the subject.</p>

    <h2>Contact Information</h2>

    <ul class="contact-list">
      <li>Email: <a href="mailto:[Your Email]">[Your Email]</a></li>
      <li>Telegram: <a href="https://t.me/vncvtkv">@vncvtkv</a></li>
      <li>GitHub: <a href="https://github.com/vncvtkv">vncvtkv</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AboutPage' // Или 'AboutPage', если вы следуете правилу именования компонентов
}
</script>

<style scoped>
.about-page {
  max-width: 800px;
  margin: 0 auto; /* Центрирование по горизонтали */
  padding: 20px;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

.about-description {
  margin-bottom: 20px;
  font-size: 1.1em;
  color: #333;
}

.contact-list {
  list-style: none;
  padding: 0;
}

.contact-list li {
  margin-bottom: 10px;
}

/* Дополнительные стили для ссылок */
a {
  color: #007bff;
  text-decoration: none; /* Убрать подчеркивание */
}

a:hover {
  text-decoration: underline; /* Добавить подчеркивание при наведении */
}
</style>