<template lang='pug'>
  .page
    b-button(@click="univ()") 대학 조회
    b-button(@click="univ()") 강의 조회
    b-button(@click="$router.push('index')") 교수 조회
</template>

<script>
export default {
  components: {
  },
  methods: {
    univ () {
      this.$router.push('index')
    }
  }
}
</script>

<style lang='stylus'>
.page
  margin auto
  text-align center
  padding 3em

b-button
  margin 2em
</style>