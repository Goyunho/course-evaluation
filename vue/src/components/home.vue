<template lang='pug'>
  #school
    router-link(to='/bu')
      #bu.button 백석대학교
</template>

<script>
export default {
  name: 'school'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='stylus' scoped>
h1, h2 
  font-weight: normal

ul 
  list-style-type: none
  padding: 0

li 
  display: inline-block
  margin: 0 10px

a 
  color: black

.button
  display inline-block
  padding 1em
  box-shadow 0 0 1px rgba(30, 30, 90, 1)
</style>
