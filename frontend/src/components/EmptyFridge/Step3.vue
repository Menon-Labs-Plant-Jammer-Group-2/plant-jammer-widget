<template>
  <div>
    <p>Hello</p>
    <div class="direction-wrapper">
      <div class="back-wrapper">
        <button @click="$emit('update:step',1)" class="next button is-success">
          <span class="icon is-small">
            <i class="fas fa-arrow-left"></i>
          </span>
          <span>Back</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Step3",
  components: {},
  props: {
    step: Number,
    chosen: Array
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
.back-wrapper {
  display: flex;
  justify-content: flex-start;
  margin-top: 1rem;
  margin-left: 2rem;
}
</style>