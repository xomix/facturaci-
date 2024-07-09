import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RegisterView from '@/views/RegisterView.vue'
import LoginView from '@/views/LoginView.vue'
import DashBoardView from '@/views/DashBoardView.vue'
import ProfileView from '@/views/ProfileView.vue'
import AppartmentView from '@/views/AppartmentView.vue'
import EditAppartmentView from '@/views/EditAppartmentView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashBoardView,
    meta: { requiresAuth: true },
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: '/appartment/:id',
    name: 'Appartment',
    component: AppartmentView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: '/editappartment/:id',
    name: 'EditAppartment',
    component: EditAppartmentView,
    meta: { requiresAuth: true },
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
