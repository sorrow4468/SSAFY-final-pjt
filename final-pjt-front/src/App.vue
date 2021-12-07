<template>
  <div id="app" style="overflow:auto">
    <Navbar/>    
    <router-view class="container"/>
  </div>
</template>

<script>
import Navbar from '@/Navbar'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  methods: {
    ...mapActions([
      'getMovies',
      'getGenres',      
      'checkLogin',
    ]),
    getToken() {
      const token = localStorage.getItem('jwt')
      return token
    },
  },
  computed: {
  },
  created() {
    this.getMovies()
    this.getGenres()
    this.$store.dispatch('checkLogin', this.getToken())
  }  
}
</script>

<style>
  @import './assets/styles/common.css';  
  @import './assets/styles/hover.css';
  @import './assets/styles/font.css';
</style>
