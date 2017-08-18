<template lang="pug">
  footer.v-footer
    span.footer-layout Developer : {{ dev }}
    span.footer-layout E-mail : {{ email }}
</template>

<script>
export default {
  data () {
    return {
      dev: 'Yoonho Go',
      email: 'rhdbsgh0629@naver.com'
    }
  }
}
</script>

<style lang="stylus">
footer.v-footer
  text-align center
  color white
  padding 1em
  background-color #2d2d2d
  padding-bottom 5em

span.footer-layout
  margin 1em
  padding 0.3em
  box-shadow 0px 0px 1px white
  border-radius 0.2em
</style>