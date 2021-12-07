<template>
  <div>
    <div class="fw-bold fs-1 pt-5 d-flex justify-content-start">Review Detail</div>
    <div v-if="reviewShow" class="pt-5">
      <b-row>          
        <b-col cols="8" class="fs-3 fw-bold d-flex justify-content-start">{{review.title}}</b-col>
        <b-col cols="2" class="d-flex justify-content-start fs-4 fw-bold">{{review.user.username}}</b-col>
        <b-col cols="2" class="fs-4 fw-bold">
          평점: <span class="text-warning">{{reviewRank}}</span>
        </b-col>
      </b-row>
      <hr style="height:5px;">
      <p class="fs-4 d-flex justify-content-start pb-5 text-break">{{review.content}}</p>
      <div class="d-flex justify-content-between">        
        <p class="fw-bold align-self-center">{{review.created_at}}</p>
        <div class="align-self-center" v-if="isLogin">
          <b-button pill variant="outline-warning border-3" 
            class="text-light fw-bold fs-6 m-3" 
            id="show-btn" 
            @click="$bvModal.show('bv-modal-example')"
          >수정
          </b-button>
          <b-button pill variant="outline-danger border-3" 
            class="text-light fw-bold fs-6 m-3" @click="deleteReview()">삭제</b-button>
          <b-modal id="bv-modal-example" hide-footer>
            <template #modal-title>
              리뷰 수정
            </template>
              <div class="d-block">
                <div>
                <b-form @submit="onSubmit" @reset="onReset" v-if="show" @submit.stop.prevent>
                  <b-form-group
                    id="input-group-1"
                    class="mb-3"          
                  >         
                    <label id="input-group-1" for="input-1">제목 : </label>
                    <b-form-input
                      id="input-1"
                      v-model="review.title"
                      type="text"
                      placeholder="제목을 입력해주세요"
                      required
                      block
                      class="mb-3"
                      :state="validation"
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
                      v-model="review.content"
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
                      v-model="rank2"
                      class="mb-3"
                    ></b-form-input>
                    <b-form-datalist id="input-list" :options="options2"></b-form-datalist>
                  </div>
                  <div class="d-flex justify-content-center">                
                    <b-button type="submit" pill variant="outline-primary border-3" class="fw-bold fs-6 m-2" @click="updateReview()">수정</b-button>
                    <b-button type="reset" pill variant="outline-danger border-3" class="fw-bold fs-6 m-2">초기화</b-button>
                  </div>
                </b-form>
              </div>          
            </div>
          </b-modal>
        </div>
      </div>
      <hr style="height:5px;">
    </div>
    <Comments :review="review"/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Comments from '@/components/community/Comments'

const rankToStar = {
  1: '★',
  2: '★★',
  3: '★★★',
  4: '★★★★',
  5: '★★★★★',
}

export default {
  name: 'ReviewsItem',
  
  components: { 
    Comments,
  },
  data() {
    return {  
      reviewShow: true,      
      show: true,
      rank2: null,
      options2: [
        { text: '★★★★★', value: 5, },
        { text: '★★★★', value: 4, },
        { text: '★★★', value: 3, },
        { text: '★★', value: 2, },
        { text: '★', value: 1, },
      ],
      reviewRank: null,
      
    }
  },
  computed:{
    ...mapState([
      'review',
      'isLogin'
    ]),        
    validation() {
      return this.review.title.length < 31
    },
    validation2() {
      return this.review.content.length < 1001
    },
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateReview() {
      // console.log(this.review.form)
      
      const form = {
        id: this.review.id,
        title: this.review.title,
        content: this.review.content,
        rank: this.rank2,
      }      
      const formsetToken = {
        form: form,
        token: this.setToken()        
      }
      this.$store.dispatch('updateReview', formsetToken)
    },
    deleteReview(){
      const idsetToken = {
        id: this.review.id,
        token: this.setToken()
      }
      this.$store.dispatch('deleteReview', idsetToken)
    },
    onSubmit(event) {
        event.preventDefault()
    },
    onReset(event) {
      event.preventDefault()
      this.form.title = null
      this.form.content = null
      this.form.rank = null
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    },
  },
  created() {
    this.reviewRank = rankToStar[this.review.rank]
  }
}
</script>

<style>
#input-2::-webkit-scrollbar {
  width: 6px;
  
}
#input-2::-webkit-scrollbar-thumb {
  width: 6px;
  background-color: gray;
  border-radius: 50px;
}

</style>