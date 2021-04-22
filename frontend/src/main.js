import Vue from "vue";
import App from "./App.vue";
import VueSocialSharing from "vue-social-sharing";

Vue.config.productionTip = false;
Vue.use(VueSocialSharing);

new Vue({
  render: (h) => h(App),
}).$mount("#app");
