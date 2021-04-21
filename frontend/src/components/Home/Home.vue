<template>
  <div>
    <div class="wrapper">
      <img class="curry-image" :src="background" />
      <button class="column button is-large empty" @click="changeState()">
        Empty your fridge
        <i class="fas fa-chevron-right"></i>
      </button>
      <small class="desc">Find recipes you can make with ingredients you have at home</small>
    </div>
    <div class="wrapper-input">
      <p class="control has-icons-right">
        <input class="input is-rounded" type="text" placeholder="Search" />
        <span class="icon is-small is-right">
          <i class="fas fa-search"></i>
        </span>
      </p>
    </div>
  </div>
</template>

<script>
import Background from "../../../assets/curry.png";
export default {
  name: "Home",
  props: {
    state: Number
  },
  components: {},
  data() {
    return {
      background: Background
    };
  },
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
  position: relative;
}
.curry-image {
  width: 100%;
  height: 100%;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.35));
}
.empty {
  margin: 0 auto;
  width: 40%;
  justify-content: center;
  align-items: center;
  height: 30%;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  font-size: 2rem;
  /* Color 5 */
  color: #e2f7cb;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  background: #459071;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 1rem;
  top: 20%;
  left: 50%;
  position: absolute;
  text-align: center;
}
@media screen and (min-width: 769px), print .columns:not(.is-desktop) {
  display: none;
}
.fridge {
  font-size: 2rem;
}
.fa-chevron-right {
  margin-left: 0.5rem;
}
.desc {
  font-size: 1rem;
  overflow-wrap: break-word;
  font-family: Bebas Neue;
  color: white;
  position: absolute;
  top: 70%;
  left: 45%;
  z-index: 4;
}
input {
  color: #49a24f;
  border: 1px solid #99d19d;
}
::placeholder {
  color: #49a24f;
}
.wrapper-input {
  width: 35%;
  margin-top: 2%;
  margin-left: 60%;
}
.fa-search {
  color: #459071;
}
</style>