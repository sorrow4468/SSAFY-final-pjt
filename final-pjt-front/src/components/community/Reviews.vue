<template>
  <div>    
    <b-row>
      <hr style="height:5px;" class="m-3">
      <!-- <b-col cols="2" class="fw-bold fs-3">영화제목</b-col>
      <b-col cols="4" class="fw-bold fs-3">게시글</b-col> -->
      <b-col cols="6" class="fw-bold fs-3">게시글</b-col>
      <b-col cols="2" class="fw-bold fs-3">작성자</b-col>
      <b-col cols="4" class="fw-bold fs-3">작성시간</b-col>
      <hr style="height:5px;" class="m-3">
    </b-row>
    <div v-if="reviews[0]">      
      <b-row v-for="review in reviews" :key="review.id" :review="review">
        <b-col class="d-flex justify-content-start" cols="6" @click="goReviewDetail(review)" style="cursor:pointer;">{{review.title}}</b-col>
        <b-col cols="2" >{{review.user.username}} </b-col>
        <b-col cols="4" >{{review.created_at}}</b-col>
        <hr class="m-3">
      </b-row>
    </div>
    <div v-else>
      <p class="fs-4 m-3">
        아직 작성된 리뷰가 없습니다
      </p>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

// import ReviewsItem from './ReviewsItem.vue'


export default {
  name: 'Reviews',
  components: {
    // ReviewsItem, 
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    goReviewDetail(reviewinfo) {
      this.$store.dispatch('goReviewDetail',reviewinfo)
    },
  },
  computed: {
    ...mapState([
      'reviews'
    ])
  },
  created() {
    this.$store.dispatch('getReviews',this.setToken())
  }

}
</script>

<style>

</style>