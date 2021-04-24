<template>
  <div>
    <p class="sub1 title is-4">SELECT AT LEAST 1 INGREDIENT</p>
    <p class="sub2 title is-6">Select ingredients you'd like to cook with</p>
    <p class="sub2 title is-6">with to create a recipe</p>
    <div class="field">
      <p v-if="chosen.length>=1" class="title is-4">The ingredients you've selected</p>
      <div class="holder">
        <p class="item" v-for="chose in holder" :key="chose['name']">
          <span class="icon">
            <img class="icon-ingredient" :src="chose['icon']" />
          </span>
          {{chose["name"]}}
        </p>
      </div>
      <div class="input-wrapper">
        <p class="control has-icons-right">
          <input
            class="input search is-rounded"
            v-model="searchQuery"
            type="text"
            placeholder="Search for ingredients ..."
            @focus="inputFocus = true"
            @blur="inputFocus = false"
          />
          <span class="icon is-small is-right">
            <i class="fas fa-search"></i>
          </span>
        </p>
      </div>
    </div>
    <div
      @mouseover="searchFocus = true"
      @mouseleave="searchFocus = false"
      v-if="inputFocus || searchFocus"
    >
      <div class="parent" v-for="ingredient in filteredIngredients" :key="ingredient['name']">
        <button class="result button is-white" @click="addIngredients(ingredient)">
          <span class="icon">
            <img class="icon-ingredient" :src="ingredient['icon']" />
          </span>
          <span>{{ingredient['name']}}</span>
        </button>
      </div>
    </div>

    <div v-if="chosen.length >= 1" class="next-wrapper">
      <button @click="$emit('update:step',1)" class="next button is-success">
        <span class="icon is-small">
          <i class="fas fa-arrow-right"></i>
        </span>
        <span>Next</span>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Step1",
  components: {},
  props: {
    step: Number,
    chosen: Array,
    holder: Array
  },
  data() {
    return {
      searchQuery: "",
      searchData: [],
      inputFocus: false,
      searchFocus: false
    };
  },
  methods: {
    addIngredients(ingredient) {
      if (!this.chosen.includes(ingredient["name"])) {
        this.holder.push(ingredient);
        this.chosen.push(ingredient["name"]);
      }
    }
  },
  async created() {
    // for populating our search data so that we can search and get the list of available options
    // while typing
    let self = this;
    axios
      .get(`http://127.0.0.1:8000/ingredient/`)
      .then(function(response) {
        let data = response.data["data"]["ingredients"];
        for (let ingredient of data) {
          self.searchData.push({
            name: ingredient["name"],
            icon: ingredient["icon"]["url"] ?? ""
          });
        }
        console.log(self.searchData);
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  computed: {
    // just pattern matches with whatever the user is typing in the input box, filters results
    // for relevant matches
    filteredIngredients: function() {
      var self = this;
      let filteredData = this.searchData.filter(function(ingredient) {
        return (
          ingredient["name"]
            .toLowerCase()
            .indexOf(self.searchQuery.toLowerCase()) >= 0
        );
      });
      return filteredData.slice(0, 6);
    }
  }
};
</script>

<style scoped>
.input-wrapper {
  width: 80%;
  margin-top: 2rem;
  text-align: center;
  margin: 2rem auto 0 auto;
}
.fa-search {
  color: #459071;
}
input {
  color: #2d5d4c;
  border: 1px solid #e2f7cb;
  position: static;
}
::placeholder {
  color: #a1c09c;
}
.icon-ingredient {
  fill: #2d5d4c;
}
.sub1 {
  font-size: 2rem;
  /* identical to box height */
  padding: 0;
  margin: 0;
  /* Color 2 */
  font-family: "Bebas Neue";
  font-style: normal;
  font-weight: 400;
  color: #459071;
}
@media screen and (min-width: 769px),
  print .steps:not(.is-vertical) .has-content-centered .steps-segment:not(:last-child) :after {
  left: 50%;
  right: -50%;
  margin: 0 !important;
}
.icon-ingredient {
  color: #2d5d4c !important;
}
.steps:not(.is-hollow) .steps-marker:not(.is-hollow) {
  background-color: #459071 !important;
  color: #fff;
}
.sub2 {
  padding: 0;
  margin: 0;
  font-style: normal;
  font-weight: normal;
  font-size: 1rem;
  color: #459071;
}
.parent {
  display: flex;
  justify-content: center;
}
.result {
  justify-content: left;
  width: 80%;
  border: none;
  color: #2d5d4c;
}
.item {
  text-align: center;
}
.next-wrapper {
  margin-top: 1rem;
  display: flex;
  justify-content: flex-end;
  margin-right: 2rem;
}
</style>