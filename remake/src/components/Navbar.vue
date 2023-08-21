<script setup>

</script>

<template>
  <header class="app-navbar">
<!--    <img src="@/assets/logo.svg" alt="Logo" class="logo" />-->
    <nav>
      <a href="/">首页</a>
      <a href="/register">注册</a>
      <a href="/login">登录</a>
      <!-- 更多链接 -->
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppNavbar',
};
</script>

<style>
.app-navbar {
  width: 100%;
  padding: 10px 23px;
  background-color: #f5f5f5;
  //box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.logo {
  width: 50px;
}

nav a {
  margin-right: 15px;
  text-decoration: none;
  color: #333;
}
</style>

