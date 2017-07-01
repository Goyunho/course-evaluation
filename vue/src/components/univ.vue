<template lang='pug'>
  #univ
    header {{univ}}
    nav
      ul 교수평가
      ul 과목평가

    article
    
</template>

<script>
export default {
  name: 'univ',
  data () {
    return {
      univ: null,
      lis: null
    }
  },
  watch: {
    '$route' (to, from) {
      this.$set(this, 'univ', to)
    }
  },
  mounted () {
    this.$http.get('http://127.0.0.1:8000/course/?format=json')
    .then((result) => {
      this.$set(this, 'lis', result.data)
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='stylus' scoped>
nav
  float left

article
  float right
</style>
