<template>
  <div>
    <div class="header-wrapper">
      <h1 class="header is-size-3">YOUR SHOPPING LIST</h1>
      <div class="banner"></div>
    </div>
    <div class="cart">
      <div>
        <div class="sub is-size-5">Ingredient</div>
        <div v-for="product in shoppingCart" class="ingredient" :key="product.name">{{product.name}}</div>
      </div>
      <div>
        <div class="sub is-size-5">Amount needed</div>
        <div
          v-for="product in shoppingCart"
          class="amount"
          :key="product.amount"
        >{{product.amount}}g</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ShoppingList",
  props: {
    shoppingCart: Array
  },
  data() {
    return {};
  }
};
</script>

<style>
.header-wrapper {
  margin-top: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  height: 6rem;
}
.header {
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.08em;
  color: #2d5d4c;
  z-index: 1;
}
.banner {
  width: 18rem;
  height: 2rem;
  background: #e2f7cb;
  position: absolute;
  margin-top: 3%;
  margin-left: 30%;
}

.ingredient {
  margin: 1rem 0;
  font-style: normal;
  font-weight: 500;
  font-size: 13px;
  line-height: 16px;
  color: #2d5d4c;
}
.amount {
  margin: 1rem 0;
  font-style: normal;
  font-weight: normal;
  font-size: 13px;
  line-height: 15px;

  /* Color 2 */

  color: #459071;
}
.cart {
  display: flex;
  justify-content: space-evenly;
}
.sub {
  color: #b1cbad;
  font-style: normal;
  font-weight: normal;
}
</style>