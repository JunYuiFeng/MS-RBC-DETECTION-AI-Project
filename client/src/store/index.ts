// store/index.ts
import { createStore } from 'vuex';

const store = createStore({
  state: {
    token: localStorage.getItem('token') || null,
    role: localStorage.getItem('role') || null,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    setRole(state, role) {
      state.role = role;
      localStorage.setItem('role', role);
    },
    clearAuth(state) {
      state.token = null;
      state.role = null;
      localStorage.removeItem('token');
      localStorage.removeItem('role');
    },
  },
  actions: {
    login({ commit }, { token, role }) {
      commit('setToken', token);
      commit('setRole', role);
    },
    logout({ commit }) {
      commit('clearAuth');
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.token,
    getToken: (state) => state.token,
    getRole: (state) => state.role,
  },
});

export default store;
