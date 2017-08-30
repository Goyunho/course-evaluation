<template lang="pug">
  article.university
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
          router-link(to="under") {{row.value}}({{row.item.name_en}})
</template>

<script>
export default {
  data () {
    return {
      items: null,
      fields: {
        name:     { label: '학교 이름', sortable: true },
      },
      sortBy: null,
      sortDesc: false,
      filter: null,
      modalDetails: { index:'', data:'' }
    }
  },
  methods: {
    show (row) {
      console.log(row)
    },
    details(item, index, button) {
      this.modalDetails.data = JSON.stringify(item, null, 2);
      this.modalDetails.index = index;
      this.$root.$emit('show::modal','modal1', button);
    },
    resetModal() {
      this.modalDetails.data = '';
      this.modalDetails.index = '';
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    }
  },
  created () {
    // console.log(this.$rout)
    var url = [this.$glob.server, 'university'].join('/')
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