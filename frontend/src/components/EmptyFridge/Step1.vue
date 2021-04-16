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
    <div>
      <li v-for="chose in chosen" :key="chose">{{chose}}</li>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Step1",
  components: {},
  data() {
    return {
      searchQuery: "",
      searchData: [],
      inputFocus: false,
      searchFocus: false,
      chosen: []
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
</style>