import PaginatedTable from './components/PaginatedTable.vue';
import Landing from './components/Landing.vue';

export const routes = [{
    path: '/',
    name: 'home',
    components: {  
      'app-landing': Landing
    }
  },
  {
    path: '/wallmart/products/:catId',
    name: 'wallmartProducts',
    components: {  
       default: Landing,
       'app-paginatedTable' : PaginatedTable
    }
  },
  {
    path: '/safeway/products/:catId',
    name: 'safewayProducts',
    components: {  
       default: Landing,
       'app-paginatedTable' : PaginatedTable
    }
  }

];
