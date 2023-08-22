<script setup>

</script>

<template>
  <div class="home-page">
    <div class="content">
    <h1>欢迎来到工作协同系统</h1>
    <p>这里是首页，你可以查看公司的最新动态和公告。</p>
    <div class="sections">
      <div class="section">
        <h2>最新动态</h2>
        <p>了解公司的最新活动、项目进展和团队成就。</p>
      </div>
      <div class="section">
        <h2>任务看板</h2>
        <p>快速访问你的待办事项，查看任务进度和协作情况。</p>
      </div>
      <div class="section">
        <h2>报告分析</h2>
        <p>查看各部门和项目的统计报告，更好地了解工作状况。</p>
      </div>
      <div class="section">
        <h2>信息订阅</h2>
        <p>订阅感兴趣的部门和项目，不错过任何重要更新。</p>
      </div>
    </div>
  </div>
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
  padding: 50px; /* 减小填充值 */
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

.sections {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.section {
  flex: 1;
  min-width: 200px;
  padding: 15px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
  margin: 10px;
  border-radius: 8px;
}

h2 {
  color: #333;
  font-weight: 600;
}
</style>
