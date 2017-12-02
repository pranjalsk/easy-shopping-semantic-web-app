<template>
  <div>
    <span>Catagory id is : {{$route.params.catId}}</span>
    <grid :data="products "  :move-pages="movePages" :start-row="startRow" :rows-per-page="rowsPerPage">
    </grid>
  </div>

</template>

<script>

function getProductsFromId(vm) {

  var sparqlQuery;
  if(vm.$route.params.catId == 4){
      sparqlQuery = `PREFIX store:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    SELECT ?storeName ?category ?productName ?productPrice
                    FROM <http://localhost:3030/easyshop/data/Store>
                    WHERE {
                        ?person store:hasStore ?storeName ;
                            store:hasCategory ?category ;
                                store:hasName ?productName ;
                                store:hasPrice ?productPrice .
                            FILTER (?storeName = "Safeway")
                              FILTER (?category = "Alcohol").
                    }`;
  }
  else if(vm.$route.params.catId == 3){
    sparqlQuery = `PREFIX store:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    SELECT ?storeName ?category ?productName ?productPrice
                    FROM <http://localhost:3030/easyshop/data/Store>
                    WHERE {
                        ?person store:hasStore ?storeName ;
                            store:hasCategory ?category ;
                                store:hasName ?productName ;
                                store:hasPrice ?productPrice .
                            FILTER (?storeName = "Safeway")
                              FILTER (?category = "Meat").
                    }`;
  }
  else if(vm.$route.params.catId == 2){
    sparqlQuery = `PREFIX store:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    SELECT ?storeName ?category ?productName ?productPrice
                    FROM <http://localhost:3030/easyshop/data/Store>
                    WHERE {
                        ?person store:hasStore ?storeName ;
                            store:hasCategory ?category ;
                                store:hasName ?productName ;
                                store:hasPrice ?productPrice .
                            FILTER (?storeName = "Safeway")
                              FILTER (?category = "Dairy").
                    }`;
  }
  else if(vm.$route.params.catId == 1){
    sparqlQuery = `PREFIX store:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                    SELECT ?storeName ?category ?productName ?productPrice
                    FROM <http://localhost:3030/easyshop/data/Store>
                    WHERE {
                        ?person store:hasStore ?storeName ;
                            store:hasCategory ?category ;
                                store:hasName ?productName ;
                                store:hasPrice ?productPrice .
                            FILTER (?storeName = "Safeway")
                              FILTER (?category = "Bakery").
                    }`;
  }
  else if(vm.$route.params.catId == 5){
    sparqlQuery = `PREFIX store:  <http://www.semanticweb.org/tusharpandit/ontologies/2017/10/EasyShop#>
                  SELECT ?storeName ?category ?productName ?productPrice
                  FROM <http://localhost:3030/easyshop/data/Store>
                  WHERE {
                      ?person store:hasStore ?storeName ;
                          store:hasCategory ?category ;
                              store:hasName ?productName ;
                              store:hasPrice ?productPrice .
                          FILTER (?storeName = "Safeway")
                            FILTER (?category = "Fruits").
                  }`;

  }

  vm.products = [];
  console.log("url is" + sparqlQuery);
  $.ajax({
    url: "http://localhost:3030/easyshop/",
    type: "GET",
    data: {
      query: sparqlQuery    
    },
    success: function(response) {
      response.results.bindings.forEach(element => {
        let tempObj = {};

        tempObj.productName = element.productName.value;
        tempObj.productCatagory = element.category.value;
        tempObj.productPrice = element.productPrice.value;
        vm.products.push(tempObj);
      });
      console.log(JSON.stringify(vm.products[0].productName));
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
