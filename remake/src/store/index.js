import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      user: null
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    clearUser(state) {
      state.user = null;
    }
  },
  actions: {
    login({ commit }, user) {
      // 假设你的登录逻辑在这里，成功后更新用户状态
      commit('setUser', user);
    },
    logout({ commit }) {
      // 假设你的登出逻辑在这里，成功后清除用户状态
      commit('clearUser');
    }
  }
});

export default store;
