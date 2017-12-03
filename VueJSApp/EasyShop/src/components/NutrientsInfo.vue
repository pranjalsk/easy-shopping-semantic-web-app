<template>
  <div>
    <NutrientsGrid :data="products "  :move-pages="movePages" :start-row="startRow" :rows-per-page="rowsPerPage">
    </NutrientsGrid>
  </div>

</template>

<script>

function getProductsFromId(vm) {

  var sparqlQuery =`PREFIX nutrient:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    SELECT ?types ?proteins ?calories ?fats ?carbohydrates
                    WHERE {
                      GRAPH <http://localhost:3030/easyshop/data/Nutrition>
                      {
                        ?person nutrient:hasType ?types ;
                                nutrient:hasProteins ?proteins ;
                                nutrient:hasCalories ?calories ;
                                nutrient:hasFats ?fats ;       
                                nutrient:hasCarbohydrates ?carbohydrates .
                      }
                    }`;

  vm.products = [];
  $.ajax({
    url: "http://localhost:3030/easyshop/",
    type: "GET",
    data: {
      query: sparqlQuery    
    },
    success: function(response) {
      response.results.bindings.forEach(element => {
        let tempObj = {};

        tempObj.productName = element.types.value;
        tempObj.proteins = element.proteins.value;
        tempObj.calories = element.calories.value;
        tempObj.fats = element.fats.value;
        tempObj.carbohydrates = element.carbohydrates.value;
        vm.products.push(tempObj);
      });

    },
    error: function(xhr) {
      alert(xhr);
    }
  });
}



export default {
  data() {
    return {    
      startRow: 0,
      rowsPerPage: 15,
      products: []
    };
  },
  created() {

  },
  methods: {
    movePages: function(amount) {
      let newStartRow = this.startRow + amount * this.rowsPerPage;
      if (newStartRow >= 0 && newStartRow < this.products.length) {
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
