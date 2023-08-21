<!--<script setup>-->
<!--import HelloWorld from './components/HelloWorld.vue'-->
<!--import TheWelcome from './components/TheWelcome.vue'-->
<!--</script>-->

<!--<template>-->
<!--  <header>-->
<!--    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />-->

<!--    <div class="wrapper">-->
<!--      <HelloWorld msg="You did it!" />-->
<!--    </div>-->
<!--  </header>-->

<!--  <main>-->
<!--    <TheWelcome />-->
<!--  </main>-->
<!--</template>-->

<!--<style scoped>-->
<!--header {-->
<!--  line-height: 1.5;-->
<!--}-->

<!--.logo {-->
<!--  display: block;-->
<!--  margin: 0 auto 2rem;-->
<!--}-->

<!--@media (min-width: 1024px) {-->
<!--  header {-->
<!--    display: flex;-->
<!--    place-items: center;-->
<!--    padding-right: calc(var(&#45;&#45;section-gap) / 2);-->
<!--  }-->

<!--  .logo {-->
<!--    margin: 0 2rem 0 0;-->
<!--  }-->

<!--  header .wrapper {-->
<!--    display: flex;-->
<!--    place-items: flex-start;-->
<!--    flex-wrap: wrap;-->
<!--  }-->
<!--}-->
<!--</style>-->
<script setup >
import Home from "@/views/HomePage.vue";
</script>

<template>
  <div id="app">
      <router-view></router-view>
  </div>
</template>

<script>
import AppNavbar from './components/Navbar.vue';
import AppFooter from './components/Footer.vue';

export default {
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

