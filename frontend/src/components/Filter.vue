<template>
  <div class="box filter-box">
    <div class="exit-wrapper">
      <button @click="$emit('update:filterClicked',false)" class="delete exit"></button>
    </div>
    <div v-if="activeFilter==='Cuisine Type'" class="cuisine-type-filter">
      <div class="cuisine-header">
        <button @click="activeFilter=''" class="back button">
          <i class="fas fa-arrow-left"></i>
        </button>
        <h1 class="cuisine-title is-size-3">Cuisine Type</h1>
      </div>
      <div class="field-wrapper">
        <button
          :class="cuisine['selected'] ?'cuisine-pill-focus button is-rounded is-white' :'cuisine-pill button is-rounded is-white'"
          v-for="cuisine in cuisineTypeFilters"
          :key="cuisine['name']"
          @click="cuisine['selected']=true"
        >{{cuisine['name']}}</button>
      </div>
      <div class="bottom">
        <button @click="reset(cuisineTypeFilters)" class="button reset">RESET</button>
        <button @click="$emit('update:filterClicked',false)" class="button done">DONE</button>
      </div>
    </div>
    <!-- we are just reusing the css classes of cuisine types -->
    <div v-if="activeFilter==='Dietary Preferences'" class="dietary-preferences-filter">
      <div class="cuisine-header">
        <button @click="activeFilter=''" class="back button">
          <i class="fas fa-arrow-left"></i>
        </button>
        <h1 class="cuisine-title is-size-3">Dietary Preferences</h1>
      </div>
      <div class="field-wrapper">
        <button
          :class="diet['selected'] ?'cuisine-pill-focus button is-rounded is-white' :'cuisine-pill button is-rounded is-white'"
          v-for="diet in dietaryPreferencesFilter"
          :key="diet['name']"
          @click="diet['selected']=true"
        >{{diet['name']}}</button>
      </div>
      <div class="bottom">
        <button @click="reset(dietaryPreferencesFilter)" class="button reset">RESET</button>
        <button @click="$emit('update:filterClicked',false)" class="button done">DONE</button>
      </div>
    </div>
    <div v-if="activeFilter===''">
      <div class="header">
        <i class="fas fa-sliders-h"></i>
        <p class="filter-title title is-3">Filter</p>
      </div>
      <li class="list-filter" v-for="miniFilter in filterButtons" :key="miniFilter">
        <div class="filter">{{miniFilter}}</div>
        <button @click="activeFilter=miniFilter" class="next button">
          <span class="icon is-small">
            <i class="fas fa-arrow-right"></i>
          </span>
        </button>
      </li>
      <li class="list-filter">
        <div class="filter">Time</div>
      </li>
      <div class="range">
        <div class="limit-1">0 minutes</div>
        <div class="limit-2">60+ minutes</div>
      </div>
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
      filterButtons: ["Cuisine Type", "Dietary Preferences"],
      time: 0,
      activeFilter: "",
      cuisineTypeFilters: [
        { name: "Indian", selected: false },
        { name: "Italian", selected: false },
        { name: "Mexican", selected: false },
        { name: "Nordic", selected: false },
        { name: "Middle Eastern", selected: false },
        { name: "Japanese", selected: false },
        { name: "French", selected: false },
        { name: "Spanish", selected: false }
      ],
      dietaryPreferencesFilter: [
        { name: "Nut-free", selected: false },
        { name: "Egg-free", selected: false },
        { name: "Gluten-free", selected: false },
        { name: "Vegan", selected: false },
        { name: "Lactose-free", selected: false },
        { name: "Diabetic", selected: false },
        { name: "FODMAPS", selected: false },
        { name: "Vegetarian", selected: false }
      ]
    };
  },
  methods: {
    filterTime(time) {
      let newTimes = this.searchData.filter(
        recipe => recipe["properties"]["time"] <= time
      );
      this.$emit("update:timeClicked", true);
      this.$emit("update:filteredTimes", newTimes);
    },
    reset(options) {
      for (let option of options) {
        option["selected"] = false;
      }
    }
  }
};
</script>

<style scoped>
.exit-wrapper {
  margin-top: 4%;
  margin-left: 90%;
}
.cuisine-title {
  color: white;
}
.cuisine-header {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}
.back {
  background: inherit;
  border: none;
}
.field-wrapper {
  padding: 1rem;
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 70%;
}
.cuisine-pill {
  margin: 0.5rem;
  color: #2d5d4c;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.cuisine-pill-focus {
  color: white;
  margin: 0.5rem;
  background: #459071;
  /* Color 5 */
  border: 1px solid #e2f7cb;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.cuisine-pill-focus:hover {
  color: white;
  background: #459071;
}
.bottom {
  display: flex;
  justify-content: space-evenly;
}
.done {
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  color: #2d5d4c;
  font-size: 2rem;
}
.reset {
  background: #58977d;
  border: 1px solid #ffffff;
  box-sizing: border-box;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 5px;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  color: #ffffff;
  font-size: 2rem;
}
.filter-title {
  margin-bottom: 2rem !important;
  padding: 0 0 0 1rem;
  text-align: left;
  font-family: Bebas Neue;
  color: white;
}
.header {
  margin-left: 1rem;
  display: flex;
  justify-content: flex-start;
}
.list-filter {
  display: flex;
  justify-content: space-between;
  align-items: center;
  list-style-type: none;
  margin-left: 1rem;
  color: white;
  margin-bottom: 1rem;
}
.filter {
  margin-right: 1rem;
  font-size: 1.5rem;
}
.fa-sliders-h {
  font-size: 2rem;
  color: white;
}
.fa-arrow-right {
  color: white;
}
.fa-arrow-left {
  color: white;
  font-size: 2rem;
}
.next {
  background: #459071;
  border: none;
  margin-right: 2rem;
}
.slider-wrapper {
  margin: 0 auto;
  width: 70%;
}
.slider {
  width: 100%;
}
.limit-1 {
  color: white;
  padding-right: 1rem;
}
.limit-2 {
  color: white;
  padding-left: 1rem;
}
.filter-box {
  position: absolute;
  z-index: 40;
  margin: 10% 0 0 50% !important;
  height: 70%;
  background: #459071;
}
.range {
  display: flex;
  justify-content: space-evenly;
}
.delete-wrapper {
  margin: 0.3rem 0 0 0.2rem;
}
</style>