<template>
  <div>
    <p class="sub title is-4">Select at least 1 ingredient</p>
    <p class="sub title is-6">Select ingredients you'd like to cook with</p>
    <p class="sub title is-6">with to create a recipe</p>
    <div class="input-wrapper">
      <input
        class="input is-rounded"
        v-model="searchQuery"
        type="text"
        placeholder="Search for ingredients ..."
        @focus="inputFocus = true"
        @blur="inputFocus = false"
      />
    </div>
    <div
      @mouseover="searchFocus = true"
      @mouseleave="searchFocus = false"
      v-if="inputFocus || searchFocus"
    >
      <div class="parent" v-for="ingredient in filteredIngredients" :key="ingredient">
        <button class="result button is-white" @click="addIngredients(ingredient)">{{ingredient}}</button>
      </div>
    </div>
    <p v-if="chosen.length>=1" class="title is-4">The ingredients you've selected</p>
    <div class="holder">
      <p class="item" v-for="chose in chosen" :key="chose">{{chose}}</p>
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
    chosen: Array
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
      if (!this.chosen.includes(ingredient)) {
        this.chosen.push(ingredient);
      }
    }
  },
  async mounted() {
    // for populating our search data so that we can search and get the list of available options
    // while typing
    let self = this;
    axios
      .get(`http://127.0.0.1:8000/ingredients/`)
      .then(function(response) {
        let data = response.data["data"]["ingredients"];
        for (let ingredient of data) {
          self.searchData.push(ingredient["name"]);
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
          ingredient.toLowerCase().indexOf(self.searchQuery.toLowerCase()) >= 0
        );
      });
      return filteredData.slice(0, 6);
    }
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
.parent {
  display: flex;
  justify-content: center;
}
.result {
  justify-content: left;
  width: 80%;
  border: none;
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