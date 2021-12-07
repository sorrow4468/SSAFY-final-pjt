<template>
  <div class="pt-5">
    <ReviewForm/>    
    <Reviews/>
  </div>
</template>

<script>
import Reviews from '@/components/community/Reviews'
import ReviewForm from '@/components/community/ReviewForm'

export default {
  name:'Community',
  components: {
    Reviews,
    ReviewForm
  }
}
</script>

<style>

</style>