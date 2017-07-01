<template lang='pug'>
  #school
    #schools(v-for="school in schools")
      .col-md-4.pb-2
        b-button(:size="''", :variant="'outline-success'", @click="link('/'+school.name_short_en)")
          | {{ school.name }}
</template>

<script>
import router from '../router'

export default {
  name: 'school',
  data () {
    return {
      schools: null
    }
  },
  methods: {
    link (url) {
      router.push(url)
    }
  },
  mounted () {
    this.$http.get('http://127.0.0.1:8000/university/?format=json')
    .then((result) => {
      this.$set(this, 'schools', result.data)
    })
  }
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
</style>
