<template>
  <div>
    <div class="wrapper">
      <button class="column button is-large empty" @click="changeState()">
        <b class="fridge">Empty your fridge</b>
        <br />
        <small class="desc">Find recipes you can make with ingredients you have at home</small>
      </button>
    </div>
    <div class="wrapper-input">
      <input class="is-rounded input" type="text" placeholder="search ..." />
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    state: Number
  },
  components: {},
  methods: {
    // moves from home page to empty our fridge page
    changeState: function() {
      return this.$emit("update:state", 1);
    }
  }
};
</script>

<style scoped>
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
</style>