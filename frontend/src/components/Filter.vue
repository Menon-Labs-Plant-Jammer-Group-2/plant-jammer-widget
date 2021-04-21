<template>
  <div class="box filter-box">
    <div class="exit-wrapper">
      <button @click="$emit('update:filterClicked',false)" class="delete exit"></button>
    </div>
    <p class="filter-title title is-3">Filter</p>
    <li class="list-filter" v-for="miniFilter in filterButtons" :key="miniFilter">
      {{miniFilter}}
      <button class="next is-inverted button is-success">
        <span class="icon is-small">
          <i class="fas fa-arrow-right"></i>
        </span>
      </button>
    </li>
    <li class="list-filter">Time</li>
    <div class="slider-wrapper">
      <input
        class="slider is-fullwidth is-medium is-success is-circle"
        step="1"
        min="0"
        max="60"
        value="0"
        type="range"
        v-model="time"
        @click="filterTime(time)"
      />
    </div>
    <div class="range">
      <div>0</div>
      <div>60+</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilterRecipe",
  props: {
    chosen: Array,
    filterClicked: Boolean,
    searchData: Array,
    filteredTimes: Array,
    timeClicked: Boolean
  },
  data() {
    return {
      searchQuery: "",
      filterButtons: [
        "Cuisine Type",
        "Dietary Preferences",
        "Dishes",
        "Occasions"
      ],
      time: 0
    };
  },
  methods: {
    filterTime(time) {
      let newTimes = this.searchData.filter(
        recipe => recipe["properties"]["time"] <= time
      );
      this.$emit("update:timeClicked", true);
      this.$emit("update:filteredTimes", newTimes);
    }
  }
};
</script>

<style scoped>
.exit-wrapper {
  margin-top: 4%;
  margin-left: 90%;
}
.filter-title {
  color: white;
}
.list-filter {
  list-style-type: none;
  margin-left: 1rem;
  color: white;
}
.next {
  color: inherit;
}
.slider-wrapper {
  margin: 0 auto;
  width: 50%;
}
.slider {
  width: 100%;
}
.filter-box {
  position: absolute;
  z-index: 40;
  margin: 10% 0 0 50% !important;
  height: 70%;
  background: #459071;
}
.range {
  margin: 0 auto 0 auto;
  width: 50%;
  display: flex;
  justify-content: space-between;
}
.delete-wrapper {
  margin: 0.3rem 0 0 0.2rem;
}
</style>