<template>
  <div class="app">
    <div class="box">
      <div class="title">Plant Jammer</div>

      <home />
      <gallery />
      <div class="footer-app">
        <button class="button bottom">
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
export default {
  name: "App",
  components: { Home, Gallery },

  data() {
    return {};
  },
  methods: {}

  // computed: {

  // }
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
.input {
  width: 35%;
  margin-top: 2%;
  margin-left: 60%;
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
