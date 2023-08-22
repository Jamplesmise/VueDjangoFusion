<script setup >
import Home from "@/views/HomePage.vue";
</script>

<template>
  <div id="app">
    <AppNavbar />
    <div class="content">
      <!-- 插入你的路由视图或其他内容 -->
      <router-view></router-view>
    </div>
    <AppFooter />
  </div>
</template>

<script>
import AppNavbar from './components/Navbar.vue';
import AppFooter from './components/Footer.vue';
//
export default {
  name: 'App',
  components: {
    AppNavbar,
    AppFooter,
  },
};
</script>

<style>
#app {
  max-width: 100%; /* 调整宽度以适应屏幕 */
  margin: 0 auto;
  padding: 20px;
}
.content {
  flex: 1; /* 使内容区域可伸缩，占用所有可用空间 */
}

/* 导航链接悬停效果 */
nav a:hover {
  color: #007bff;
}

/* 通用按钮样式 */
button {
  padding: 10px 20px;
  cursor: pointer;
}

/* 通用表单样式 */
form {
  margin: 20px 0;
}

input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  box-sizing: border-box;
}

button {
  padding: 10px 20px;
  cursor: pointer;
}
</style>

