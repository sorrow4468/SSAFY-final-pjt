import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'
import Detail from '@/views/movies/Detail'
import MovieList from '@/views/movies/MovieList'
import Community from '@/views/community/Community'
import ReviewsItem from '@/components/community/ReviewsItem'
import Recommend from '@/views/recommend/Recommend'

Vue.use(VueRouter)

const routes = [  
  {
    path: '/',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/detail/:movieId/',
    name: 'Detail',
    component: Detail,
  },
  {
    path: '/community/',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/:reviewId',
    name: 'ReviewsItem',
    component: ReviewsItem,
  },
  {
    path: '/recommend/',
    name: 'Recommend',
    component: Recommend,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
