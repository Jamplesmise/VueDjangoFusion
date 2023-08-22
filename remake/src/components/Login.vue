<template>
  <div class="login-page">
    <h1>登录</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="用户名" required />
      <input type="password" v-model="password" placeholder="密码" required />
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
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

const username = ref('');
const password = ref('');

const login = async () => {
  const credentials = {
    username: username.value,
    password: password.value
  };

  // 获取CSRF令牌
  const csrfToken = getCsrfToken();

  try {
    const response = await axios.post(
      'http://localhost:8000/api/userservice/login/',
      JSON.stringify(credentials),
      {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken // 在此处添加CSRF令牌
        },
      }
    );

    console.log('登录成功:', response.data);
    // 在这里添加登录成功后的逻辑，例如重定向到主页面
    window.localStorage.setItem('isAuthenticated', 'true'); // 保存登录状态
    router.push('/');
  } catch (error) {
    console.error('登录失败:', error);
    if (error.response) {
      console.error('响应数据:', error.response.data);
    } else {
      console.error('没有响应数据');
    }
  }
};
</script>


<style>
.login-page {
  width: 450px;
  margin: 150px auto;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
  border-radius: 5px;
}

.login-page h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.login-page input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.login-page button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
  border-radius: 3px;
}

.login-page button:hover {
  background-color: #0056b3;
}
</style>
