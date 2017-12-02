<template>
  <div id="app">
         <!-- Fixed navbar -->
    
    <router-view name="app-landing"></router-view>
    <br/>  
    <br/>  
    <br/>  
    <br/>  
    <br/>
    <br/>
    <div id="main">
            <div class="container-fluid" style="height:700px">
                <div class="row content" style="height:100%;">
                    <div class="col-md-3" style="height:100%;">
                              <img src="./assets/img1.jpg" style="height:100%;" > 
                    </div>
                    <div class="col-md-9" style="height:100%;">
                            <transition name="slide" mode="out-in">
                                <router-view name="animation-box"></router-view>   
                            </transition>

                            <transition name="slide" mode="out-in">
                                <router-view name="app-paginatedTable" :key="$route.fullPath"></router-view>   
                                <router-view name="app-safewayTable" :key="$route.fullPath"></router-view>   
                                <router-view name="app-safewayLocations" :key="$route.fullPath"></router-view>   
                                <router-view name="app-walmartLocations" :key="$route.fullPath"></router-view>   
                                <router-view name="app-NutrientsInfo" :key="$route.fullPath"></router-view>   
                            </transition>
                    </div>
                </div> 
            </div>
    </div>  

   
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      
    }
  }
}
</script>

<style>
img {
    max-width:100%;
    max-height:100%;
}
</style>
