<template lang="pug">
  .sign
    .nosign(v-show="who.no")
      | 아이디
      b-form-input.sign-input()
      | 패스워드
      b-form-input.sign-input(type="password")
      b-button(@click="toggle()") 버튼
    .signin(v-show="who.in")
    .signup(v-show="who.up")
</template>

<script>
export default {
  data () {
    return {
      who: {
        no: true,
        in: false,
        up: false
      },
      no: true
    }
  },
  methods: {
  }
}
</script>

<style lang="stylus">
.sign
  display inline

.sign-input
  display inline
  margin 0.5em
  width 10em
</style>