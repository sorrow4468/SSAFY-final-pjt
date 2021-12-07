import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import event from '@/assets/js/event.js'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(event)
Vue.use(SequentialEntrance)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
