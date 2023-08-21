<template>
  <div class="register-page">
    <h1>注册</h1>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="用户名" required />
      <input type="password" v-model="password" placeholder="密码" required />
      <input type="password" v-model="confirmPassword" placeholder="确认密码" required />
      <button type="submit">注册</button>
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
const confirmPassword = ref('');

const register = async () => {
  if (password.value !== confirmPassword.value) {
    alert('密码不一致！');
    return;
  }

  const credentials = {
    username: username.value,
    password: password.value
  };

  // 获取CSRF令牌
  const csrfToken = getCsrfToken();

  try {
    const response = await axios.post(
      'http://localhost:8000/api/userservice/register/',
      credentials,
      {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken // 在此处添加CSRF令牌
        },
      }
    );

    console.log('注册成功:', response.data);
    // 在这里添加注册成功后的逻辑，例如重定向到登录页面
   router.push('/login');
  } catch (error) {
    console.error('注册失败:', error);
    if (error.response) {
      console.error('响应数据:', error.response.data);
    } else {
      console.error('没有响应数据');
    }
  }
};
</script>

<style>
.register-page {
  width: 500px;
  margin: 120px auto; /* 增加顶部边距以居中页面 */
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9; /* 添加背景颜色 */
  border-radius: 8px; /* 添加圆角 */
}

/* 可以添加更多样式来定制输入框、按钮等 */
.input-field {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>

