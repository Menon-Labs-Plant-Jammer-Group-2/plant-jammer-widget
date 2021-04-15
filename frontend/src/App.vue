<template>
  <div class="app">
    <div class="box">
      <div v-if="state!==1" class="title">Plant Jammer</div>

      <home v-if="state===0" :state.sync="state" />
      <gallery v-if="state===0" :state.sync="state" />
      <empty-fridge v-if="state===1" :state.sync="state" />

      <div class="footer-app">
        <button class="button bottom" @click="state=0">
          <i class="fas fa-home" />
        </button>
        <button class="button bottom">
          <i class="fas fa-shopping-cart" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Home from "./components/Home/Home.vue";
import Gallery from "./components/Home/Gallery.vue";
import EmptyFridge from "./components/EmptyFridge/EmptyFridge.vue";
export default {
  name: "App",
  components: { Home, Gallery, EmptyFridge },

  data() {
    return {
      state: 0 // 0 for home, 1 for empty your fridge, 2 for search dishes
    };
  },
  methods: {}
};
</script>

<style>
.app {
  margin-top: 5%;
}
.box {
  width: 50%;
  margin: 0 auto;
  padding: 0;
}
.title {
  padding-top: 2rem;
  text-align: center;
}
.wrapper {
  height: 30%;
}

.empty {
  margin: 0 auto;
  width: 70%;
  justify-content: center;
  align-items: center;
  height: 100%;
}
@media screen and (min-width: 769px), print .columns:not(.is-desktop) {
  display: none;
}
.fridge {
  font-size: 2rem;
}
.desc {
  font-size: 1rem;
  overflow-wrap: break-word;
}
.bottom {
  margin-top: 2rem;
  width: 50%;
  height: 90%;
}
.fas {
  font-size: 2rem;
}
</style>
