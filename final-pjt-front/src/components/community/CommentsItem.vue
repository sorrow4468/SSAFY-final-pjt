<template>
  <div v-if="comment.review.id===review.id">  
    <b-row v-if="show">
      <b-col cols="2" class="fs-6 fw-bold d-flex justify-content-start align-items-center">{{comment.user.username}}</b-col>
      <b-col cols="4" class="fs-6 fw-bold d-flex text-break justify-content-start align-items-center">{{comment.content}}</b-col>    
      <b-col cols="3" class="fs-6 fw-bold d-flex justify-content-start align-items-center">{{comment.created_at}}</b-col> 
      <b-col cols="3" class="fs-6 fw-bold d-flex justify-content-start align-items-center">
        <b-button pill variant="outline-warning border-3" 
          class="text-light fw-bold fs-6 m-2 w-100" @click="showToggle">
          수정
        </b-button>
        <b-button pill variant="outline-danger border-3" 
          class="text-light fw-bold fs-6 m-2 w-100" @click="deleteComment">
          삭제
        </b-button>
      </b-col>
    </b-row>
    <b-row v-else>
      <b-col cols="2" class="fs-6 fw-bold d-flex justify-content-start align-items-center">{{comment.user.username}}</b-col>
      <b-col cols="6">
        <b-form-input v-model="comment.content" type="text" class="fs-6 fw-bold w-100 d-flex justify-content-center align-items-center mt-2" required></b-form-input>
      </b-col>
      <b-col cols="3" offset="1" class="d-flex justify-content-start align-items-center">
        <b-button 
          pill variant="outline-warning border-3" 
          class="text-light fw-bold fs-6 m-2 w-100" @click="updateComment">
          수정
        </b-button>
        <b-button pill variant="outline-danger border-3" 
          class="text-light fw-bold fs-6 m-2 w-100" @click="deleteComment">
          삭제
        </b-button>
      </b-col>
    </b-row>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommentsItem',
  props: {
    comment: {
      type: Object,
    },
    review: {
      type: Object,
    }
  },
  data(){
    return {
      show: true,
    }
  },
  methods:{
    showToggle(){
      return this.show = !this.show
    },
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateComment(){
      const commentdata = {
        commentId: this.comment.id,
        reviewId: this.review.id,
        content: {
          content: this.comment.content
        },
        token: this.setToken()
      }
      this.$store.dispatch('updateComment',commentdata)
      this.showToggle()
    },
    deleteComment(){
      const commentdata = {
        commentId: this.comment.id,
        token: this.setToken()
      }
      this.$store.dispatch('deleteComment',commentdata)
    }
  }, 
}
</script>

<style>

</style>