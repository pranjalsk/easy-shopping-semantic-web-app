<template>
<div style="height:100%;">
  <div style="height:80%; overflow-y:auto;">
  <table class="table table-striped">
    <thead class="h4">
      <th>Store Address</th>
      <th>Store ZIP</th>
      <th>Store Type</th>
      <th>Store Latitude</th>
      <th>Store Longitude</th>
    </thead>
    <tbody>
      <tr v-for="product in limitBy(data,rowsPerPage,startRow)">
        <td>{{ JSON.stringify(product.address) }}</td>
        <td>{{ JSON.stringify(product.zip) }}</td>
        <td>{{ JSON.stringify(product.type) }}</td>
        <td>{{ JSON.stringify(product.latitude) }}</td>
        <td>{{ JSON.stringify(product.longitude) }}</td>
      </tr>
    </tbody>
  </table>
  </div>
  <div id="page-navigation">
    <button type="button" class="btn btn-outline-dark btn-sm" @click="movePages(-1)">Back</button>
    <p>{{startRow / rowsPerPage + 1}} out of {{Math.ceil(data.length / rowsPerPage)}}</p>
    <button type="button" class="btn btn-outline-dark btn-sm" @click="movePages(1)">Next</button>
  </div>
</div>
</template>


<script>
export default {
  props: {
    data: Array,
    movePages: Function,
    startRow: Number,
    rowsPerPage: Number
  },

  methods:{
    limitBy(data,rowsPerPage,startRow) {
        if(startRow > 0 && startRow <= data.length){
            rowsPerPage = startRow + rowsPerPage;
        }
        data = data.slice(startRow, rowsPerPage)
        return data;
    }
  }
}
</script>


<style>
#page-navigation {
    display: -webkit-flex; /* Safari */
    -webkit-align-items: center; /* Safari 7.0+ */
    align-items: center;
}

#page-navigation p {
  margin-top: 10px;
  margin-left: 15px;
  margin-right: 15px;
}

</style>
