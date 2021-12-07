<template>  
  <div id="nav" class="d-flex justify-content-between fixed-top" style="background-color:#1b1b1b !important; height:90px;">
    <div> 
      <router-link :to="{ name:'MovieList' }" class="fs-2 text-decoration-none">홈</router-link> |       
      <router-link :to="{ name:'Community' }" class="fs-4 text-decoration-none">커뮤니티</router-link> | 
      <router-link :to="{ name:'Recommend' }" class="fs-4 text-decoration-none">영화추천</router-link>
    </div>
    <div class="position-absolute translate-middle top-50 start-50">
      <router-link :to="{ name:'MovieList' }" class="fs-2 text-decoration-none">
        <p style="color:#ff9999; font-family: 'Montserrat', sans-serif; font-size: 52px;" 
          class="mt-4">MOVINUS</p>
      </router-link>
    </div>
    <div class="mt-3">      
      <span v-if="isLogin">
        <router-link @click.native="logout()" to="#" class="fs-5 text-decoration-none">로그아웃</router-link>
      </span>
      <span v-if="!isLogin">
        <router-link :to="{ name:'Login' }" class="fs-5 text-decoration-none">로그인</router-link> | 
        <router-link :to="{ name:'Signup' }" class="fs-5 text-decoration-none">회원가입</router-link>
      </span>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Navbar',
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
    getToken() {
      const token = localStorage.getItem('jwt')
      return token
    },
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  computed: {
    ...mapState([
      'isLogin'
    ])
  },
  
}
</script>

<style>
  @import './assets/styles/common.css';
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300&display=swap');
</style>
