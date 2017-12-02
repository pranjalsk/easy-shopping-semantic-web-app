<template>
  <div>
    <span>Catagory id is : Walmart</span>
    <grid :data="products "  :move-pages="movePages" :start-row="startRow" :rows-per-page="rowsPerPage">
    </grid>
  </div>

</template>

<script>

import axios from "axios";

function getPapersFromId(vm){
    let catId = vm.$route.params.catId
    axios
    .get(`http://localhost:8081/domains/`+catId)
    .then(response => {
      vm.products = response.data.products;
    })
    .catch(err => {
      vm.errors.push(err);
    });
}



export default {
  data() {
    return {    
      startRow: 0,
      rowsPerPage: 5,
      products: []
    };
  },
  created() {

  },
  methods: {
    movePages: function(amount) {
      let newStartRow = this.startRow + amount * this.rowsPerPage;
      console.log(newStartRow);
      if (newStartRow >= 0 && newStartRow < this.papers.length) {
        this.startRow = newStartRow;
      }
    },
    resetStartRow: function() {
      this.startRow = 0;
    }
  },
  created(){

      getProductsFromId(this);
  },
  watch:{
      '$route'(to,from){
        this.catId = to.params.catId;

      }
  }
};
</script>


<style>

</style>
