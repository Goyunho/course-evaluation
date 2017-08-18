<template lang="pug">
  .v-header
    #logo logo
    sign

</template>

<script>
import Sign from 'components/Sign'

export default {
  components: {
    Sign
  }
}
</script>

<style lang="stylus">
.v-header
  background-color #fefefe
  padding 0.3em
  box-shadow 0em 0em 0.1em black

#logo
  display inline
</style>