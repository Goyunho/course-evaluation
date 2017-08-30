<template lang="pug">
  article.faculty
    .col-md-6d-6
      .my-1.row
        .col-md-6
          b-form-fieldset(horizontal, label="Filter", :label-cols="3", label-text-align="center")
            b-form-input(v-model="filter", placeholder="Type to Search")
        .col-sm-4.text-md-right
          b-button(:disabled="!sortBy", @click="sortBy = null") Clear Sort

      b-table(striped, hover, show-empty,
            :items="items",
            :fields="fields",
            :filter="filter",
            :sort-by.sync="sortBy",
            :sort-desc.sync="sortDesc",
            @filtered="onFiltered")

        template(slot="name", scope="row") 
          router-link(to="course") {{row.value}}
</template>

<script>
export default {
  data () {
    return {
      items: null,
      fields: {
        photo:    { lable: '사진'},
        name:     { label: '교수명', sortable: true },
        age:      { label: '나이', sortable: true},
        email:    { label: '이메일', sortable: true},
        phone:    { label: '전화번호', sortable: true},
        belong:    { label: '소속', sortable: true}
      },
      sortBy: null,
      sortDesc: false,
      filter: null,
      modalDetails: { index:'', data:'' }
    }
  },
  created () {
    // console.log(this.$rout)
    var url = [this.$glob.server, 'faculty'].join('/')
    this.$http.get(url+'/', {
      params: {
        format: 'json'
      }
    })
    .then(response => {
      // this.$set(this, 'items', response.data)
      this.items = response.data
    })
    .catch(error => {
      console.log('===================error====================')
      console.log(error)
    })
  }
}
</script>

<style lang="stylus">
</style>