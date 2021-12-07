<template>
  <b-row v-if="isLogin">
    <b-col cols="10">      
      <b-form-input type="text" 
        placeholder="댓글을 입력해주세요." 
        v-model="form.content" 
        @keyup.enter="createComment" 
        maxlength="200"
        class="m-2 w-100"></b-form-input>
    </b-col>
    <b-col cols="2">      
      <b-button pill variant="outline-success border-3" 
          class="text-light fw-bold fs-6 m-2 w-100" @click="createComment">작성
      </b-button>
    </b-col>
  </b-row>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name:'CommentForm',
  props:{
    review:{
      type:Object
    }
  },
  data(){
    return {
      form:{
        content:null,
      }
    }
  },
  computed:{
    ...mapState([
      'isLogin'
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
    createComment() {
      const formsetToken = {
        content: this.form,
        reviewId: this.review.id,
        token: this.setToken()
      }
      this.$store.dispatch('createComment', formsetToken)
      this.form.content = null
    }
  }
}
</script>

<style>

</style>