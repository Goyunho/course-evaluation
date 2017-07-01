<template lang='pug'>
    #app
        img(src="./assets/logo.png")
        router-view
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang='stylus'>
#app 
    font-family 'Avenir', Helvetica, Arial, sans-serif
    -webkit-font-smoothing antialiased
    -moz-osx-font-smoothing grayscale
    text-align center
    color black
    margin-top 60px

</style>
