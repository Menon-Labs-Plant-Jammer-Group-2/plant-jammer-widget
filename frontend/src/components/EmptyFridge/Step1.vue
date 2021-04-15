<template>
  <div>
    <p class="sub title is-4">Select at least 1 ingredient</p>
    <p class="sub title is-6">Select ingredients you'd like to cook with</p>
    <p class="sub title is-6">with to create a recipe</p>
    <div class="input-wrapper">
      <input class="input is-rounded" type="text" placeholder="Search for ingredients ..." />
    </div>
  </div>
</template>

<script>
export default {
  name: "Step1",
  components: {},
  data() {
    return {};
  }
};
</script>

<style scoped>
.input-wrapper {
  margin-top: 2rem;
  text-align: center;
}
.input {
  width: 80%;
  margin: 0 auto;
}
.sub {
  padding: 0;
  margin: 0;
}
</style>