<template lang='pug'>
  .page
    b-button(@click="$router.push({name:'university'})") 대학 조회
    b-button(@click="$router.push({name:'faculty'})") 교수 조회
    b-button(@click="$router.push({name:'course'})") 강의 조회
</template>

<script>
export default {

}
</script>

<style lang='stylus'>
.page
  margin auto
  text-align center
  padding 10em

button
  margin 0.5em
</style>