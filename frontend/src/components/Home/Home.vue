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
    <div class="wrapper-level">
      <div class="browse">BROWSE DISHES</div>
      <div class="wrapper-input">
        <p class="control has-icons-right">
          <input class="input is-rounded" type="text" placeholder="Search keywords ..." />
          <span class="icon is-small is-right">
            <i class="fas fa-search"></i>
          </span>
        </p>
      </div>
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
  height: 15rem;
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: flex-end;
  justify-content: flex-end;
  padding-left: 55%;
  margin-right: 20%;
}
.curry-image {
  position: absolute;
  width: 100%;
  height: 15rem;
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.35));
}
.empty {
  margin-right: 10%;
  margin-left: 10%;
  width: 30%;
  height: 5rem !important;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  font-size: 2em;
  /* Color 5 */
  color: #e2f7cb;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  background: #459071;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 1rem;
  position: relative;
  text-align: center;
  z-index: 2;
  width: fit-content;
}
.empty:hover {
  background: #2d5d4c;
}
@media screen and (min-width: 769px), print .columns:not(.is-desktop) {
  display: none;
}
.fridge {
  font-size: 2rem;
}
.fa-chevron-right {
  margin-left: 0.5rem;
  position: relative;
}
.desc {
  font-size: 1.2rem;
  overflow-wrap: break-word;
  font-family: Bebas Neue;
  color: white;
  position: relative;
  z-index: 4;
  padding-bottom: 10%;
  padding-right: 5%;
}
.browse {
  font-family: Bebas Neue;
  font-size: 2rem;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.05em;
  color: #2d5d4c;
  margin: 0 auto;
}
input {
  color: #49a24f;
  border: 1px solid #99d19d;
}
::placeholder {
  color: #49a24f;
}
.wrapper-level {
  display: flex;
  align-items: center;
  margin-top: 2%;
}
.wrapper-input {
  margin-left: 15%;
  margin-right: 10%;
}
.fa-search {
  color: #459071;
}
</style>