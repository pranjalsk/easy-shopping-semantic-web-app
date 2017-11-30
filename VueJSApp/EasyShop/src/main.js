import Vue from 'vue';
import App from './App.vue';
import PaginatedTable from './components/PaginatedTable.vue';
import Landing from './components/Landing.vue';
import VueRouter from 'vue-router';

import { routes } from './routes';

Vue.use(VueRouter);

Vue.component('app-landing', Landing );
Vue.component('app-paginatedTable', PaginatedTable );

const router = new VueRouter({
    routes: routes,
    mode:'history'
  });



new Vue({
  el: '#app',
  router:router,
  render: h => h(App)
})
