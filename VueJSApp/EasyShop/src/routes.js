import PaginatedTable from './components/PaginatedTable.vue';
import SafewayTable from './components/SafewayTable.vue';
import SafewayLocations from './components/SafewayLocations.vue';
import walmartLocations from './components/walmartLocations.vue';
import NutrientsInfo from './components/NutrientsInfo.vue';
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
    path: '/walmart/products/:catId',
    name: 'walmartProducts',
    components: {  
      'app-landing': Landing,
       'app-paginatedTable' : PaginatedTable
    }
  },
  {
    path: '/safeway/products/:catId',
    name: 'safewayProducts',
    components: {  
      'app-landing': Landing,
       'app-safewayTable' : SafewayTable
    }
  },
  {
    path: '/safeway/locations',
    name: 'safewayLocations',
    components: {  
      'app-landing': Landing,
       'app-safewayLocations' : SafewayLocations
    }
  },
  {
    path: '/walmart/locations',
    name: 'walmartLocations',
    components: {  
      'app-landing': Landing,
       'app-walmartLocations' : walmartLocations
    }
  },
  {
    path: '/NutrientsInfo',
    name: 'NutrientsInfo',
    components: {  
      'app-landing': Landing,
       'app-NutrientsInfo' : NutrientsInfo
    }
  }

];
