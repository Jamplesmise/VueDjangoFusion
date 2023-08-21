<script setup>

</script>

<template>
  <div class="home">
    <Navbar />
    <div class="content">
      <h1>欢迎来到主页</h1>
      <p>这是你的公司或项目的主页。</p>
      <a href="/about">了解更多</a>
    </div>
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'Home',
  components: {
    Navbar,
    Footer
  },
  methods: {
    showLoginDialog() {
      // 显示登录对话框逻辑
    },
    showRegisterDialog() {
      // 显示注册对话框逻辑
    }
  }
}
</script>

<style>
.home-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.content {
    flex: 1 1 auto; /* 可自由伸缩，占据剩余空间 */
    text-align: center;
    padding: 275px;
}
.home-page h1 {
  font-size: 2rem;
  color: #333;
}

.home-page p {
  font-size: 1rem;
  color: #666;
  line-height: 1.5;
}

.home-page a {
  color: #007bff;
  text-decoration: none;
}

.home-page a:hover {
  text-decoration: underline;
}
</style>
