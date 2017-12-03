<template>
  <div>
    <LocationsGrid :data="products "  :move-pages="movePages" :start-row="startRow" :rows-per-page="rowsPerPage">
    </LocationsGrid>
  </div>

</template>

<script>

function getProductsFromId(vm) {

  var sparqlQuery =`PREFIX location:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    PREFIX locationName:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/9/EasyShop#>
                    SELECT ?location ?latitude ?longitude ?address ?zip 
                    FROM <http://localhost:3030/easyshop/data/Location>
                    WHERE {
                        ?person locationName:hasLocation ?location ;
                            location:hasLatitide ?latitude ;
                                location:hasLongitude ?longitude ;
                                location:hasAddress ?address ;
                                location:hasZip ?zip .
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

        tempObj.address = element.address.value;
        tempObj.zip = element.zip.value;
        tempObj.type = element.location.value;
        tempObj.latitude = element.latitude.value;
        tempObj.longitude = element.longitude.value;
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
