<template>
  <div class="app">
    <div class="box">
      <div class="main title">Plant Jammer</div>

      <div class="footer-app">
        <div class="bottom-wrapper">
          <button
            :class="state===1 || state===0 || state===2 ? 'button bottom-active' : 'button bottom'"
            @click="state=0"
          >HOME</button>
          <div :class="state===1 || state===0 || state === 2? 'bottom-line-active' : 'bottom-line'"></div>
        </div>
        <div class="bottom-wrapper">
          <button
            :class="state===3 ? 'button bottom-active' : 'button bottom'"
            @click="state=3"
          >SHOPPING LIST</button>
          <div :class="state===3? 'bottom-line-active' : 'bottom-line'"></div>
        </div>
      </div>

      <home v-if="state===0" :state.sync="state" />
      <gallery v-if="state===0" :stsate.sync="state" />
      <empty-fridge v-if="state===1" :state.sync="state" :shoppingCart.sync="shoppingCart" />
      <shopping-list v-if="state===3" :state.sync="state" :shoppingCart.sync="shoppingCart" />
    </div>
  </div>
</template>

<script>
import Home from "./components/Home/Home.vue";
import Gallery from "./components/Home/Gallery.vue";
import EmptyFridge from "./components/EmptyFridge/EmptyFridge.vue";
import ShoppingList from "./components/ShoppingList.vue";
export default {
  name: "App",
  components: { Home, Gallery, EmptyFridge, ShoppingList },

  data() {
    return {
      state: 0, // 0 for home, 1 for empty your fridge, 2 for search dishes
      shoppingCart: []
    };
  },
  methods: {}
};
</script>

<style>
.footer-app {
  display: flex;
  justify-content: center;
  align-items: center;
}
.app {
  margin-top: 5%;
}
.box {
  width: 50%;
  margin: 0 auto;
  padding: 0;
  position: relative;
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
.bottom-wrapper {
  width: 50%;
  display: flex;
  flex-direction: column;
}
.bottom {
  width: 100%;
  margin: 0 auto;
  text-align: center;
  font-family: "Bebas Neue";
  font-size: 1.5rem;
  color: #8f8f8f;
  border: none;
  outline: none;
}
.bottom-active {
  width: 100%;
  margin: 0 auto;
  text-align: center;
  font-family: "Bebas Neue";
  font-size: 1.5rem;
  color: #13816f;
  border: none;
  outline: none;
}
.bottom-line {
  width: 100%;
  height: 0.15rem;
  background: #2d5d4c;
}
.bottom-line-active {
  width: 100%;
  height: 0.3rem;
  background: #2d5d4c;
}
.main {
  height: 6rem;
  font-family: "Oleo Script Swash Caps";
  color: #ffffff;
  background: radial-gradient(
      80% 5657.02% at 98.51% 65.91%,
      #2d5d4c 37.19%,
      #459071 100%
    ),
    linear-gradient(180deg, #2d5d4c 0%, #459071 99.99%, #e2f7cb 100%);
}
.block:not(:last-child),
.box:not(:last-child),
.breadcrumb:not(:last-child),
.content:not(:last-child),
.highlight:not(:last-child),
.level:not(:last-child),
.list:not(:last-child),
.message:not(:last-child),
.notification:not(:last-child),
.pagination:not(:last-child),
.progress:not(:last-child),
.subtitle:not(:last-child),
.table-container:not(:last-child),
.table:not(:last-child),
.tabs:not(:last-child),
.title:not(:last-child) {
  margin: 0;
}
</style>
