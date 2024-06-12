import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import store from '@/store';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
    meta: {
      authRequired: false,
      adminRequired: false,
    },
  },
  {
    path: '/detect',
    name: 'RBCDetection',
    component: () => import('../views/RBCDetection.vue'),
    meta: {
      authRequired: true,
      adminRequired: false,
    },
  },
  {
    path: '/about',
    name: 'about',
    component: () =>
      import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
    meta: {
      authRequired: true,
      adminRequired: false,
    },
  },
  {
    path: '/comparison',
    name: 'Comparison',
    component: () => import('../views/CompareView.vue'),
    meta: {
      authRequired: true,
      adminRequired: false,
    },
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/AdminView.vue'),
    meta: {
      authRequired: true,
      adminRequired: true,
    },
  },
  {
    path: '/404',
    name: 'Unauthorized',
    component: () => import('../views/UnauthorizedView.vue'),
    meta: {
      authRequired: false,
      adminRequired: false,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Routes Guard
router.beforeEach((to, from, next) => {
  const role = store.getters.getRole;

  // If the user is authenticated and trying to access the login page
  if (role && to.name === 'Login') {
    return next({ name: 'RBCDetection' });
  }

  if (to.meta.authRequired) {
    if (!role) {
      // If user is not authenticated, redirect to Unauthorized
      return next({ name: 'Unauthorized' });
    }

    if (to.meta.adminRequired && role !== 'ADMIN') {
      // If the route requires admin access and the user is not an admin
      return next({ name: 'Unauthorized' });
    }
  }

  // For routes that don't require authentication or if user has proper access
  return next();
});

export default router;
