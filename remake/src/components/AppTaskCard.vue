<template>
  <div>
    <h1>任务管理</h1>
<!--      加载-->
    <button @click="fetchTasks">加载任务</button>
<!--      创建-->
    <button @click="showCreateForm = true">创建任务</button>
    <div v-if="showCreateForm">
      <input v-model="newTask.title" placeholder="标题" />
      <textarea v-model="newTask.description" placeholder="描述"></textarea>
      <input type="date" v-model="newTask.deadline" placeholder="截止日期" />
      <select v-model="newTask.priority">
        <option value="low">低</option>
        <option value="medium">中</option>
        <option value="high">高</option>
      </select>
      <select v-model="newTask.status">
        <option value="not_started">未开始</option>
        <option value="in_progress">进行中</option>
        <option value="completed">已完成</option>
      </select>
      <select v-model="newTask.depends_on">
        <option value="" disabled selected>选择依赖任务</option>
        <option v-for="task in tasks" :value="task.id">{{ task.title }}</option>
      </select>
      <select v-model="newTask.assigned_to">
        <option value="" disabled selected>选择用户</option>
        <option v-for="user in users" :value="user.id">{{ user.username }}</option>
      </select>
      <!-- 使用库如 vue-multiselect 或自定义多选组件 -->
      <multiselect v-model="newTask.tags" :options="tags" multiple></multiselect>

      <!-- 添加更多字段 -->
      <button @click="createTask">创建</button>
      <button @click="showCreateForm = false">取消</button>
    </div>
<!--      删除-->
    <ul>
      <li v-for="task in tasks" :key="task.id" v-if="task">
        {{ task.title }} - {{ task.description }}
        <button @click="deleteTask(task.id)">删除</button>
        <!-- 可以添加编辑按钮和其他操作 -->
      </li>
    </ul>
<!--      修改-->
   <!-- 更新任务表单 -->
    <div v-if="updateTask">
      <input v-model="updateTask.title" placeholder="标题" />
      <!-- 其他字段的输入元素 -->
      <button @click="updateSelectedTask">保存</button>
      <button @click="cancelUpdateTask">取消</button>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
      newTask: {
      title: '',
      description: '',
      deadline: null, // 可以使用日期选择器
      priority: 'medium',
      status: 'not_started',
      // 其他可能需要的字段
      depends_on: null, // 默认不依赖任何任务
      assigned_to: null, // 默认不分配给任何用户
      updateTask: null, // 当前正在编辑的任务
      tags: [], // 已选标签
    },
      showCreateForm: false,
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await axios.get('http://localhost:8000/api/task_service/');
        this.tasks = response.data;
        console.log('Fetched tasks:', this.tasks); // 添加此行来调试
      } catch (error) {
        console.error('获取任务失败:', error);
      }
    },
    async createTask() {
      try {
        await axios.post('http://localhost:8000/api/task_service/', this.newTask);
        await this.fetchTasks(); // 刷新任务列表
        this.showCreateForm = false;
        this.newTask = { title: '', description: '' }; // 清空表单
      } catch (error) {
        console.error('创建任务失败:', error);
      }
    },
    async deleteTask(taskId) {
      try {
        await axios.delete(`http://localhost:8000/api/task_service/${taskId}/`);
        await this.fetchTasks(); // 刷新任务列表
      } catch (error) {
        console.error('删除任务失败:', error);
      }
    },
    // 可以添加更新和其他操作的方法
  },
  async updateTask() {
    try {
      await axios.put(`http://localhost:8000/api/task_service/${this.editingTask.id}/`, this.editingTask);
      await this.fetchTasks(); // 刷新任务列表
      this.editingTask = null; // 清空正在编辑的任务
    } catch (error) {
      console.error('更新任务失败:', error);
    }
  },
  startEditingTask(task) {
    this.editingTask = { ...task }; // 创建任务的副本以进行编辑
  },
  cancelEditingTask() {
    this.editingTask = null; // 取消编辑
  },

  mounted() {
    this.fetchTasks(); // 初始化时加载任务
  },
};
</script>

<style>
.task-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
}

.status {
  color: #333;
}

.deadline {
  color: #888;
}
</style>
