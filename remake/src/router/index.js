import {createRouter, createWebHistory} from "vue-router";
import ProtectedPage from '@/views/ProtectedPage.vue';
const isAuthenticated = window.localStorage.getItem('isAuthenticated') === 'true';
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomePage.vue') // 根据实际文件路径配置组件
  },
  {
    path: '/register/',
    name: 'Register',
    component: () => import('../components/Register.vue')
  },
  {
    path: '/login/',
    name: 'Login',
    component: () => import('../components/Login.vue')
  },
  // 其他路由配置
  {
        path: '/activity',
        name: 'Activity',
        component:() => import('../views/ActivityPage.vue')
    },
    {
        path: '/tasks',
        name: 'Tasks',
        component: () => import('../views/TasksPage.vue')
    },
    {
        path: '/reports',
        name: 'Reports',
        component: () => import('../views/ReportsView.vue')
    },
    {
        path: '/settings',
        name: 'Settings',
        component: () => import('../views/UserSettingsPage.vue')
    },
     {
    path: '/protected',
    component: () => import('../views/ProtectedPage.vue'),
    beforeEnter: (to, from, next) => {
      if (!isAuthenticated) {
        next('/login'); // 重定向到登录页面
      } else {
        next();
      }
    },
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;