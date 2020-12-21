import Vue from 'vue'
import App from './App.vue'
import router from './router'


// -------------------------------------------------------
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faFire, faCloudUploadAlt, faPlus, faUser, faSmileWink, faStoreAlt, faSortAmountDown, faEllipsisV, faCog, faTrash, faUserPlus} from '@fortawesome/free-solid-svg-icons'
Vue.component('FontAwesomeIcon', FontAwesomeIcon);
library.add(faFire, faCloudUploadAlt, faPlus, faUser, faSmileWink, faStoreAlt, faSortAmountDown, faEllipsisV, faCog, faTrash, faUserPlus)
// -------------------------------------------------------

import VueSweetalert2 from 'vue-sweetalert2';
Vue.use(VueSweetalert2);

// CONFIGURO O BOOTSTRAP
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)


import Select2 from 'v-select2-component';
Vue.component('Select2', Select2);


// ------------------------------
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  Select2
}).$mount('#app')