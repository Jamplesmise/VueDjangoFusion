import store from '../store/index.js';

export const authGuard = (to, from, next) => {
  const isAuthenticated = store.getters['auth/isAuthenticated'];

  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ name: 'LoginPage' });
  } else {
    next();
  }
};
