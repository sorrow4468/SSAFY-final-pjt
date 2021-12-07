<template>
  <div>
    <h1 style="padding-top:220px;">회원가입을 환영합니다!</h1>    
    <div class="d-flex justify-content-center">
      <b-form style="width:400px;" @submit.stop.prevent>        
        <b-form-input class="rounded-pill mt-3" style="height:50px;" id="username" v-model="credentials.username" required placeholder="아이디"></b-form-input>
        <b-form-input class="rounded-pill mt-3" style="height:50px;" v-model="credentials.password" type="password" id="password" aria-describedby="password-help-block" placeholder="비밀번호"></b-form-input>
        <b-form-input class="rounded-pill mt-3" style="height:50px;" :state="validation" v-model="credentials.passwordConfirmation" type="password" id="passwordConfirmation" aria-describedby="password-help-block" @keyup.enter="signup" placeholder="비밀번호 확인"></b-form-input>    
        <b-form-invalid-feedback v-if="this.credentials.passwordConfirmation" :state="validation">
          비밀번호가 일치하지 않습니다
        </b-form-invalid-feedback>
        <b-form-valid-feedback v-if="this.credentials.passwordConfirmation" :state="validation">
          비밀번호가 일치합니다
        </b-form-valid-feedback>
        <b-button class="rounded-pill mt-3 w-100" style="height:50px;" @click="signup" variant="success">회원가입</b-button>
      </b-form>
    </div>
    <p class="m-3">가입 후 로그인 페이지로 이동합니다</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  computed: {
    validation() {
      return this.credentials.password === this.credentials.passwordConfirmation
    },
  },
  methods: {
    signup() {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
      .then(
        this.$router.push({ name:'Login' })
      )
      .catch(
        err => console.log(err)
      )
    }
  }
}
</script>

<style>

</style>