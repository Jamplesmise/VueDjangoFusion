import Home from '@/views/HomePage.vue';
import Register from '../components/Register.vue';
import Login from '../components/Login.vue';
import {createRouter, createWebHistory} from "vue-router";
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register/',
    name: 'Register',
    component: Register
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  // 其他路由配置
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
export default router;