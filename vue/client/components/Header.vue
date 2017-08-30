<template lang="pug">
  .v-header
    router-link(to="/") 홈페이지
    navi
    sign

</template>

<script>
import Navi from 'components/Navi'
import Sign from 'components/Sign'

export default {
  components: {
    Navi,
    Sign
  }
}
</script>

<style lang="stylus">
.v-header
  background-color #fefefe
  padding 0.3em
  box-shadow 0em 0em 0.1em black
</style>