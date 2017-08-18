<template lang="pug">
  .index
    v-header
    router-view
    v-footer
</template>

<script>
import Home from 'views/Home'
import Header from 'components/Header'
import Footer from 'components/Footer'

export default {
  components: {
    'v-header': Header,
    'v-footer': Footer
  }
}
</script>

<style lang="stylus">
#router-aria
  padding 1em
  margin 1em
  text-align: center
  background-color white
  box-shadow 0em 0em 0.1em black
  border-radius 0.5em
</style>