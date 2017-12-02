import PaginatedTable from './components/PaginatedTable.vue';
import SafewayTable from './components/SafewayTable.vue';
import SafewayLocations from './components/SafewayLocations.vue';
import Landing from './components/Landing.vue';
import AnimatedBox from './components/AnimatedBox.vue';

export const routes = [{
    path: '/',
    name: 'home',
    components: {  
      'app-landing': Landing,
      'animation-box': AnimatedBox
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
       'app-safewayTable' : SafewayTable
    }
  },
  {
    path: '/safeway/locations',
    name: 'safewayLocations',
    components: {  
       default: Landing,
       'app-safewayLocations' : SafewayLocations
    }
  }

];
