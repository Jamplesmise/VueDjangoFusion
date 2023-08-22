<template>
  <div class="protected-page">
    <h1>受保护的页面</h1>
    <p>只有已登录的用户才能看到这个页面的内容。</p>
    <!-- 在此处添加你想展示给已登录用户的任何其他内容 -->
  </div>
</template>

<script>
export default {
  name: 'ProtectedPage',
  // 可以添加任何你需要的脚本，例如获取数据的方法
};
</script>

<style>
/* 可以添加任何你想要的样式来美化页面 */
.protected-page {
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
}
</style>
