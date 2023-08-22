<script setup>
</script>

<template>
  <nav>
      <!-- 更多链接 -->
      <ul class="navbar">
      <li
        v-for="(route, index) in routes"
        :key="index"
        @mouseenter="setActive(index)"
        @mouseleave="clearActive"
      >
        <router-link :to="route.path">{{ route.name }}</router-link>
      </li>
      <li class="dropdown" @mouseenter="showDropdown = true" @mouseleave="clearDropdown">
        <a href="#" class="dropdown-toggle">{{ isAuthenticated ? '已登录' : '未登录' }}</a>
        <ul class="dropdown-menu" v-if="showDropdown">
          <li v-if="!isAuthenticated"><a href="/login/">登录</a></li>
          <li v-if="!isAuthenticated"><a href="/register/">注册</a></li>
          <li v-if="isAuthenticated"><a href="#" @click="logout">登出</a></li>
        </ul>
      </li>
      </ul>
  </nav>

</template>

<script>



// import { ref } from 'vue';
import axios from 'axios';
import router from "@/router";

// 获取CSRF令牌的函数
function getCsrfToken() {
  const name = 'csrftoken';
  const value = '; ' + document.cookie;
  const parts = value.split('; ' + name + '=');
  if (parts.length === 2) {
    return parts.pop().split(';').shift();
  }
}

export default {
    name: 'AppNavbar',
  data() {
    return {
      routes: [
        { name: '主页', path: '/' },
        { name: '任务', path: '/tasks' },
        { name: '动态', path: '/activity' },
        { name: '设置', path: '/settings' },
        { name: '报告', path: '/reports'},
        // 添加其他导航项
      ],
      activeIndex: null,
      showDropdown: false,
      isAuthenticated: false // 认证状态，可以根据实际情况更改
    };
  },
  computed: {
    isAuthenticated() {
      return window.localStorage.getItem('isAuthenticated') === 'true'; // 获取登录状态

    },
  },

  watch: {
    isAuthenticated: {
      handler() {
        this.$forceUpdate(); // 强制组件重新渲染
      },
      deep: true,
    },
  },

  methods: {
    setActive(index) {
      this.activeIndex = index;
    },
    clearActive() {
      this.activeIndex = null;
    },
    clearDropdown() {
      this.showDropdown = false;
    },

  async logout() {
  const csrfToken = getCsrfToken(); // 获取CSRF令牌，与登录相同
  console.log("CSRF Token:", csrfToken); // 打印CSRF令牌
  console.log(document.cookie);
  try {
    // 输出数字888，表示登出成功
    // console.log(888);

    // await axios.post('http://localhost:8000/api/userservice/logout/', null, {
      await axios.get('http://localhost:8000/api/userservice/logout/', {
      headers: {
        'X-CSRFToken': csrfToken // 在此处添加CSRF令牌
      },
    });
    // console.log(888);
    window.localStorage.removeItem('isAuthenticated');
    router.push('/login');
    this.isAuthenticated = false;
    this.showDropdown = false;
  } catch (error) {
    alert('登出失败，请稍后再试。');
  }
}


  }

};
</script>

<style scoped>
.navbar {
  list-style: none;
  padding: 10px 0;
  margin: 0;
  display: flex;
  border-radius: 10px;
  justify-content: space-around;
  background-color: #008E9B;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

.navbar li {
  list-style: none;
  padding: 10px;
  text-align: center;
  transition: background-color 0.1s;
  border-radius: 10px;
}

.navbar li.active {
  background-color: #00CADC;
  color: #ffffff; /* 选中时的文字颜色 */
}

.navbar li a {
  color: #333333;
  font-size: 16px;
  font-family: 'Arial', sans-serif;
  text-decoration: none;
  display: block;
}


</style>
