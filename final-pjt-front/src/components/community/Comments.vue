<template>
  <div class="">
    <div class="fw-bold fs-3 d-flex justify-content-start">댓글</div>
    <CommentForm :review="review"/>
    <b-row class="mt-3">
      <b-col cols="2" class="d-flex justify-content-start fs-5 fw-bold">작성자</b-col>
      <b-col cols="4" class="d-flex justify-content-start fs-5 fw-bold">내용</b-col>
      <b-col cols="3" class="d-flex justify-content-start fs-5 fw-bold">작성시간</b-col>
      <b-col cols="3" class="d-flex justify-content-start"></b-col>
    </b-row>
    <hr style="height:5px;">
    <div v-if="comments[0]">  
      <CommentsItem v-for="comment in comments" :key="comment.id" :comment="comment" :review="review"/>
    </div>
    <div v-else>
      <p class="fs-4 m-3">
        아직 작성된 댓글이 없습니다
      </p>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import CommentForm from '@/components/community/CommentForm'
import CommentsItem from '@/components/community/CommentsItem'

export default {
  name:'Comments',
  components: {
    CommentForm,
    CommentsItem,
  },  
  props:{
    review:{
      type:Object,
    }
  },
  computed: {
    ...mapState([
      'comments',
    ]),
    ...mapGetters([
      'comments'
    ])
  },
  methods:{
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getComments(){
      const reviewIdsetToken = {
        reviewId: this.review.id,
        token: this.setToken()
      }
      this.$store.dispatch('getComments',reviewIdsetToken)
    }
  },
  created(){
    this.getComments()
  }
}
</script>

<style>

</style>