<template>
  <div class="box fridge-box">
    <div class="exit-wrapper">
      <button @click="$emit('update:fridgeClicked',false)" class="delete exit"></button>
    </div>
    <p class="fridge-title title is-3">Your fridge</p>
    <div v-if="!noIngredients">
      <div class="input-wrapper has-icons-right">
        <input
          class="input fridge-input is-rounded"
          v-model="searchQuery"
          type="text"
          placeholder="Search"
        />
      </div>
      <div class="holder">
        <div class="item" v-for="chose in filteredData" :key="chose">
          <p>{{chose}}</p>
          <div class="delete-wrapper">
            <button @click="removeIngredient(chose)" class="delete"></button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h1>You have no more ingredients left! :(</h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Fridge",
  props: {
    chosen: Array,
    fridgeClicked: Boolean,
    searchData: Array
  },
  data() {
    return {
      searchQuery: "",
      noIngredients: false
    };
  },
  methods: {
    removeIngredient: function(ingredient) {
      let newChosen = this.chosen.filter(item => item != ingredient);
      console.log(newChosen);
      this.$emit("update:chosen", newChosen);
      let self = this;
      if (newChosen.length >= 1) {
        let url = "http://127.0.0.1:8000/recipes/?";
        let selected = JSON.parse(JSON.stringify(newChosen));

        for (let ingredient of selected) {
          ingredient = ingredient.split(" ").join("");
          url += `q=${ingredient}&`;
        }
        url = url.slice(0, url.length - 1); // to remove the extra & since that would mess with our backend
        axios
          .get(url)
          .then(function(response) {
            let data = response.data["data"]["dishes"];
            let newSearchData = [];
            for (let dish of data) {
              let properties = {
                properties: {
                  name: dish["name"],
                  time: dish["estimatedPreparationTime"],
                  image: dish["image"]["url"]
                }
              };
              newSearchData.push(properties);
            }
            console.log(newSearchData);
            self.$emit("update:searchData", newSearchData);
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        let noMore = [];
        this.$emit("update:searchData", noMore);
        this.noIngredients = true;
      }
    }
  },
  computed: {
    filteredData: function() {
      var self = this;
      let filteredData = this.chosen.filter(function(ingredient) {
        return (
          ingredient.toLowerCase().indexOf(self.searchQuery.toLowerCase()) >= 0
        );
      });
      return filteredData;
    }
  }
};
</script>

<style scoped>
.exit-wrapper {
  margin-top: 4%;
  margin-left: 90%;
}

.fridge-box {
  position: absolute;
  z-index: 40;
  margin: 10% 0 0 50% !important;
  height: 70%;
  background: #459071;
}
.fridge-title {
  color: white;
  font-weight: 10;
  margin-bottom: 2rem !important;
  padding-top: 0 !important;
}
.input-wrapper {
  width: 80%;
  margin: 0 auto 2rem auto;
  display: flex;
}
.item {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
}
.fridge-input {
  background: inherit;
  color: white;
}
::placeholder {
  color: white;
}

.delete-wrapper {
  margin: 0.3rem 0 0 0.2rem;
}
</style>