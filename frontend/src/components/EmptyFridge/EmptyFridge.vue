<template>
  <div>
    <fridge
      v-if="fridgeClicked"
      :fridgeClicked.sync="fridgeClicked"
      :chosen.sync="chosen"
      :searchData.sync="searchData"
    />

    <filter-recipe
      v-if="filterClicked"
      :filterClicked.sync="filterClicked"
      :chosen.sync="chosen"
      :searchData.sync="searchData"
      :timeClicked.sync="timeClicked"
      :filteredTimes.sync="filteredTimes"
    />
    <div class="header">
      <div class="empty title">Empty Your Fridge</div>
      <div class="highlight"></div>
      <!-- make this responsive -->
      <button class="button back" @click="$emit('update:state',0)">&lt; BACK</button>
    </div>
    <div class="steps-wrapper">
      <ul class="steps has-content-above has-content-centered">
        <li
          v-for="(dot,index) in steps"
          :class="index === step ? 'steps-segment is-active' : 'steps-segment' "
          :key="dot"
        >
          <a href="#" class="steps-marker"></a>
          <div class="steps-content">
            <p class="step is-size-6">{{dot}}</p>
          </div>
        </li>
      </ul>
    </div>
    <step1 :chosen="chosen" :step.sync="step" :holder.sync="holder" v-if="step===0" />
    <step2
      :fridgeClicked.sync="fridgeClicked"
      :filterClicked.sync="filterClicked"
      :chosen.sync="chosen"
      :step.sync="step"
      :searchData.sync="searchData"
      :filteredTimes.sync="filteredTimes"
      :timeClicked.sync="timeClicked"
      :selectedDish.sync="selectedDish"
      :suggestedNames.sync="suggestedNames"
      v-if="step===1"
    />
    <step3
      :callbackEmit="callbackEmit"
      :selectedDish.sync="selectedDish"
      :chosen.sync="chosen"
      :step.sync="step"
      v-if="step===2"
    />
  </div>
</template>

<script>
import Step1 from "./Step1.vue";
import Step2 from "./Step2.vue";
import Step3 from "./Step3";
import Fridge from "./Fridge.vue";
import FilterRecipe from "../Filter.vue";
export default {
  name: "EmptyFridge",
  components: {
    Step1,
    Step2,
    Step3,
    Fridge,
    FilterRecipe
  },
  props: {
    state: Number
  },
  data() {
    return {
      step: 0,
      chosen: [],
      steps: ["Select ingredients", "Choose dish", "Finalize"],
      fridgeClicked: false,
      filterClicked: false,
      searchData: [],
      filteredTimes: [],
      timeClicked: false,
      selectedDish: "",
      suggestedNames: new Set(),
      holder: []
    };
  },
  methods: {
    callbackEmit(newChosen) {
      this.chosen = newChosen;
      // this.$emit("update:chosen", newChosen);
    }
  }
};
</script>

<style scoped>
.header {
  position: relative;
}
.empty {
  position: relative;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  left: 15%;
  font-size: 3rem;
  z-index: 10;
  letter-spacing: 0.08em;
  color: #2d5d4c;
}
.highlight {
  position: absolute;
  width: 55%;
  height: 40%;
  left: 22%;
  top: 70%;
  z-index: auto;
  background: #e2f7cb;
}
.button {
  background-color: inherit; /* Green */
  outline: none;
  box-shadow: none;
  color: white;
}
.back {
  position: absolute;
  top: -130%;
  font-size: 1.5rem;
  margin-left: 1rem;
  font-family: Bebas Neue;
  border: none;
}
.input-wrapper {
  margin-top: 2rem;
  text-align: center;
}
.input {
  width: 80%;
  margin: 0 auto;
}
.steps-wrapper {
  text-align: center;
  margin-top: 1.5rem;
  margin-bottom: 2rem;
}
.steps {
  margin: 0 auto;
  width: 80%;
}
.steps:not(.is-hollow) .steps-segment.is-active .steps-marker:not(.is-hollow) {
  /* color: #fff; */
  background: #b5e4ad;
  transform: scale(0.6);
}
.steps:not(.is-hollow)
  .steps-segment.is-active
  ~ .steps-segment
  .steps-marker:not(.is-hollow) {
  border: 2px solid #b5e4ad;
  background: #f9f9f9;
  transform: scale(0.6);
}
li.steps-segment::after {
  margin: 0;
  background: #e2f7cb;
}
.step {
  color: #2d5d4c;
}
li.steps-segment.is-active::after {
  margin: 0;
  background: #e2f7cb;
}
.sub {
  padding: 0;
  margin: 0;
}
</style>