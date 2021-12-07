<template>
  <div>
    <div class="d-flex justify-content-around">             
      <div name="findGenreNames" v-for="(findGenreName,idx) in findGenreNames" :key="idx">
        <b-button pill 
          variant="outline-danger"
          class="fs-4 text-light border-4" 
          @click="getGenreMovies(findGenreName['id'])" id="movieGenre">{{ findGenreName['name'] }}</b-button>        
      </div>
    </div>
    <div v-if="randomMovies" class="d-flex justify-content-between">
      <div v-for="(randomMovie,idx) in randomMovies.slice(0, 5)" :key="idx" style="cursor:pointer"> 
        <sequential-entrance>          
          <div @click="goMovieDetail(randomMovie)" class="banner_img">          
            <img class="m-3 w-100 duration" :src="imgSrc + randomMovie.poster_path" :alt="randomMovie.title"
              style="width:192px; height:292px; object-fit:fill;"
            >
          </div>
        </sequential-entrance>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import methods from '@/assets/js/event.js'

export default {
  
  name: 'MovieDetailRecommend',
  computed: {
    ...mapState([
      'genres',
      'randomMovies',      
      'genreMovies',
      'findGenreNames',    
      'imgSrc',  
    ])
  },
  watch: {

  },
  methods: {
    ...mapActions([      
      'getGenreMovies',
      'findGenreName',
      'goMovieDetail',
    ]),    
  },
  created() {
    this.findGenreName()    
  },
  mounted() {
    methods.clickRandomMovie()
  }
  
}
</script>

<style>

</style>