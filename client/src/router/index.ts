import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import store from '@/store';
// import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'RBCDetection',
    component: () => import('../views/RBCDetection.vue'),
    meta: {
      authRequired: false,
    },
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    meta: {
      authRequired: false,
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
    meta: {
      authRequired: false,
    },
  },
  {
    path: '/comparison',
    name: 'Comparison',
    component: () => import('../views/CompareView.vue'),
    meta: {
      authRequired: false,
    },
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/AdminView.vue'),
    meta: {
      authRequired: true,
    },
  },
  {
    path: '/',
    name: 'Unauthorized',
    component: () => import('../views/UnauthorizedView.vue'),
    meta: {
      authRequired: false,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  //check page protection
  if (to.meta.authRequired) {
    //get contact's id
    const role = store.getters.getRole
    //access check
    if (role === 'ADMIN') {
      return next();
    } else {
      router.push({
        name: 'Unauthorized',
      });
    }
  } else {
    return next();
  }
});

export default router
