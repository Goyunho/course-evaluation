<template lang='pug'>
  #bu
    header 백석대학교
    nav
      ul 교수평가
      ul 과목평가

    article
      | 목록
      #list(v-for='li in lis')
        | {{ li.name }}

    
</template>

<script>
export default {
  name: 'bu',
  data () {
    return {
      lis: null
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
</style>
