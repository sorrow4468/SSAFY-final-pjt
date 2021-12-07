<template>
  <div class="d-flex justify-content-between">
    <div class="fw-bold fs-1">Review</div>
    <div v-if="isLogin">
      <b-button pill variant="outline-warning border-3" 
        class="text-light fw-bold fs-6" 
        id="show-btn" 
        @click="$bvModal.show('bv-modal-example')"
      >리뷰 작성
      </b-button>
      <b-modal id="bv-modal-example" hide-footer>
        <template #modal-title>
          리뷰 작성
        </template>
          <div class="d-block">
            <div>
            <div class="close"></div>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show" @submit.stop.prevent>
              <b-form-group
                id="input-group-1"
                class="mb-3"          
              >         
                <label id="input-group-1" for="input-1">제목 : </label>
                <b-form-input
                  id="input-1"
                  v-model="form.title"
                  type="text"
                  placeholder="제목을 입력해주세요"
                  required
                  block
                  class="mb-3"
                  :state="validation"
                  max
                ></b-form-input>
                <b-form-invalid-feedback :state="validation">
                  제목이 30자를 초과하였습니다
                </b-form-invalid-feedback>
                <b-form-valid-feedback :state="validation">
                  제목을 30자 이내로 적어주세요
                </b-form-valid-feedback>
              </b-form-group>

              <b-form-group id="input-group-2" label="내용:" label-for="input-2" @submit.stop.prevent>
                <b-form-textarea
                  id="input-2"
                  v-model="form.content"
                  placeholder="내용을 입력해주세요"
                  required
                  rows="3"
                  max-rows="6"
                  class="mb-3"
                  :state="validation2"
                ></b-form-textarea>
                <b-form-invalid-feedback :state="validation2">
                  내용이 1000자를 초과하였습니다
                </b-form-invalid-feedback>
                <b-form-valid-feedback :state="validation2">
                  내용을 1000자 이내로 적어주세요
                </b-form-valid-feedback>
              </b-form-group>

              <div>
                <label for="input-with-list">평점</label>
                <b-form-input list="input-list" id="input-with-list" 
                  placeholder="평점을 입력해주세요"
                  v-model="form.rank"
                  class="mb-3"
                ></b-form-input>
                <b-form-datalist id="input-list" :options="options"></b-form-datalist>
              </div>
              <div class="d-flex justify-content-center">                
                <b-button type="submit" pill variant="outline-success border-3" class="fw-bold fs-6 m-2" @click="createReview">리뷰 작성</b-button>
                <b-button type="reset" pill variant="outline-danger border-3" class="fw-bold fs-6 m-2">초기화</b-button>
              </div>
            </b-form>
          </div>          
        </div>
      </b-modal>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ReviewForm',
  data(){
    return{
      form: {
        title: '',
        content: '',
        rank: '',
      },
      show: true,
      options: [
        { text: '★★★★★', value: 5, },
        { text: '★★★★', value: 4, },
        { text: '★★★', value: 3, },
        { text: '★★', value: 2, },
        { text: '★', value: 1, },
      ]
    }
  },
  computed: {
    validation() {
      return this.form.title.length < 31
    },
    validation2() {
      return this.form.content.length < 1001
    },
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
    createReview() {      
      const formsetToken = {
        form: this.form,
        token: this.setToken()
      }
      this.$store.dispatch('createReview', formsetToken)
      this.form.title = ''
      this.form.content = ''
      this.form.rank = ''
    },
    onSubmit(event) {
        event.preventDefault()
        alert('작성하신 리뷰가 등록되었습니다!')
      },
    onReset(event) {
      event.preventDefault()
      this.form.title = ''
      this.form.content = ''
      this.form.rank = null
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
    toggle() {
      this.show = !this.show
    }
  }
}
</script>

<style>
.close{
  background-color: transparent;
  border:0px;
  font-size: 1.5rem;
}
</style>