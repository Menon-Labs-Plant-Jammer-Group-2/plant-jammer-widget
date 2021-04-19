<template>
  <div>
    <fridge
      v-if="fridgeClicked"
      :fridgeClicked.sync="fridgeClicked"
      :chosen.sync="chosen"
      :searchData.sync="searchData"
    />
    <div class="header">
      <div class="title">Empty Your Fridge</div>
      <!-- make this responsive -->
      <button class="button is-white back" @click="$emit('update:state',0)">&lt; Back to home</button>
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
            <p class="is-size-6">{{dot}}</p>
          </div>
        </li>
      </ul>
    </div>
    <step1 :chosen="chosen" :step.sync="step" v-if="step===0" />
    <step2
      :fridgeClicked.sync="fridgeClicked"
      :chosen.sync="chosen"
      :step.sync="step"
      :searchData.sync="searchData"
      v-if="step===1"
    />
    <step3 :chosen="chosen" :step.sync="step" v-if="step===2" />
  </div>
</template>

<script>
import Step1 from "./Step1.vue";
import Step2 from "./Step2.vue";
import Step3 from "./Step3";
import Fridge from "./Fridge.vue";
export default {
  name: "EmptyFridge",
  components: {
    Step1,
    Step2,
    Step3,
    Fridge
  },
  props: {
    state: Number
  },
  data() {
    return {
      step: 0,
      chosen: [],
      steps: ["Common ingredients", "Choose dish", "Finalize"],
      fridgeClicked: false,
      filterClicked: false,
      searchData: []
    };
  }
};
</script>

<style scoped>
.header {
  position: relative;
}
.back {
  position: absolute;
  top: 2rem;
  margin-left: 1rem;
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
  margin-bottom: 2rem;
}
.steps {
  margin: 0 auto;
  width: 80%;
}
.sub {
  padding: 0;
  margin: 0;
}
</style>