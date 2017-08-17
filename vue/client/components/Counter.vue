<template lang="pug">
  .counter-wrapper
    .counter
      | {{ count }}
    b-button(:variant="'primary'", @click="$store.commit('INCREMENT')") Increment
    b-button(@click="$store.commit('DECREMENT')") Decrement
    b-button(@click="$store.dispatch('incrementAsync')") Increment Async
</template>

<script>
export default {
  computed: {
    count() {
      return this.$store.state.count
    }
  }
}
</script>

<style lang="stylus">
.counter 
  margin: 100px auto
  border-radius: 3px
  width: 200px
  height: 200px
  text-align: center
  line-height: 200px
  font-size: 5rem
  background-color: #f0f0f0
  user-select: none
</style>
