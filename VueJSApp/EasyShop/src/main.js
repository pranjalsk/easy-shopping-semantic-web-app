import Vue from 'vue';
import App from './App.vue';
import PaginatedTable from './components/PaginatedTable.vue';
import SafewayTable from './components/SafewayTable.vue';
import SafewayLocations from './components/SafewayLocations.vue';
import walmartLocations from './components/walmartLocations.vue';
import NutrientsInfo from './components/NutrientsInfo.vue';
import AnimatedBox from './components/AnimatedBox.vue';
import Landing from './components/Landing.vue';
import VueResource from 'vue-resource'
import Grid from './components/Grid.vue';
import NutrientsGrid from './components/NutrientsGrid.vue';
import LocationsGrid from './components/LocationsGrid.vue';
import VueRouter from 'vue-router';

import { routes } from './routes';

Vue.use(VueRouter);
Vue.use(VueResource);

Vue.component('app-landing', Landing );
Vue.component('app-paginatedTable', PaginatedTable );
Vue.component('app-safewayTable', SafewayTable );
Vue.component('app-AnimatedBox', AnimatedBox );
Vue.component('app-SafewayLocations', SafewayLocations );
Vue.component('app-walmartLocations', walmartLocations );
Vue.component('app-NutrientsInfo', NutrientsInfo );
Vue.component('NutrientsGrid', NutrientsGrid );
Vue.component('LocationsGrid', LocationsGrid );
Vue.component('grid', Grid );

const router = new VueRouter({
    routes: routes,
    mode:'history'
  });



new Vue({
  el: '#app',
  router:router,
  render: h => h(App)
})
