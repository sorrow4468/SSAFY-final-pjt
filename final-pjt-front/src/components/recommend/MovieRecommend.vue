<template>
  <div class="pt-5">
    <div class="d-flex justify-content-around flex-wrap">      
      <div name="genres" v-for="(genre,idx) in genres" :key="idx" class="m-2">        
        <b-button pill variant="outline-danger border-3" class="text-light fw-bold fs-6"
          @click="getGenreMovies(genre.id)">
          {{ genre['name']}}          
        </b-button>
      </div>
    </div>
    <hr style="color:#ff9999; height:5px;">
    <b-row class="d-flex" v-if="randomMovies">      
      <b-col cols="3" v-for="randomMovie in randomMovies" :key="randomMovie.id" style="cursor:pointer">
        <sequential-entrance fromTop>          
          <div @click="goMovieDetail(randomMovie)" class="banner_img duration">          
            <img :src="imgSrc+randomMovie.poster_path" alt="포스터 이미지" class="w-75 m-3"
              style="width:229px; height:344px; object-fit:cover;"
            >
          </div>
        </sequential-entrance>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'MovieRecommend',
  computed: {
    ...mapState([
      'genres',
      'genreMovies',
      'randomMovies',
      'imgSrc',
      'isLogin'
    ])
  },
  methods: {
    ...mapActions([      
      'getGenreMovies',
      'goMovieDetail',
    ]),
    checkLogin(){
      if(!this.isLogin){
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name: 'Login'})
      }
    }
  },
  mounted(){
    this.checkLogin()
  }
}
</script>

<style scoped>
.duration {
  animation-duration: 800ms !important;
}

</style>