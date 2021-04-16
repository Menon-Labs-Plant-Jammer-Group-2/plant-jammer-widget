<template>
  <div>
    <div v-if="searchData.length!=0">
      <div class="search-dishes">
        <input class="input is-rounded" v-model="searchQuery" type="text" placeholder="Search" />
      </div>
      <div class="metadata">
        <button class="filter-button button is-white">Filter</button>
        <button class="fridge-button button is-white">Your fridge</button>
      </div>
      <div class="scrollbar">
        <div class="dish-results" v-for="dish in filteredDishes" :key="dish['properties']['name']">
          <div class="card">
            <div class="card-image">
              <img :src="dish['properties']['image']" alt="Placeholder image" />
              <div class="name">
                <p class="title is-4">{{dish["properties"]["name"]}}</p>
              </div>
            </div>
            <div class="content">
              Time
              <div class="time">{{dish['properties']["time"]}} minutes</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="searchData.length==0">
      <h1 class="title">We weren't able to find any dishes with your ingredients :(</h1>
    </div>
    <div class="direction-wrapper">
      <div class="back-wrapper">
        <button @click="$emit('update:step',0)" class="next button is-success">
          <span class="icon is-small">
            <i class="fas fa-arrow-left"></i>
          </span>
          <span>Back</span>
        </button>
      </div>
      <div class="next-wrapper">
        <button @click="$emit('update:step',2)" class="next button is-success">
          <span class="icon is-small">
            <i class="fas fa-arrow-right"></i>
          </span>
          <span>Next</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Step2",
  components: {},
  props: {
    step: Number,
    chosen: Array
  },
  data() {
    return {
      searchData: [],
      searchQuery: ""
    };
  },
  async mounted() {
    /* Here we just get the generated recipes of the ingredients that we had 
    from step 1  */
    let self = this;
    let url = "http://127.0.0.1:8000/recipes/?";
    let selected = JSON.parse(JSON.stringify(this.chosen));

    for (let ingredient of selected) {
      ingredient = ingredient.split(" ").join("");
      url += `q=${ingredient}&`;
    }
    url = url.slice(0, url.length - 1); // to remove the extra & since that would mess with our backend
    axios
      .get(url)
      .then(function(response) {
        let data = response.data["data"]["dishes"];
        for (let dish of data) {
          let properties = {
            properties: {
              name: dish["name"],
              time: dish["estimatedPreparationTime"],
              image: dish["image"]["url"]
            }
          };
          self.searchData.push(properties);
        }
        let found = JSON.parse(JSON.stringify(self.searchData));
        self.results = found.length >= 1 ? true : false;
      })
      .catch(function(error) {
        console.log(error);
      });
  },
  computed: {
    filteredDishes: function() {
      var self = this;
      let filteredData = this.searchData.filter(function(dish) {
        let temp = JSON.parse(JSON.stringify(dish));
        console.log(temp);
        temp = temp["properties"]["name"];
        console.log(temp);
        return temp.toLowerCase().indexOf(self.searchQuery.toLowerCase()) >= 0;
      });
      return filteredData.slice(0, 6);
    }
  }
};
</script>

<style scoped>
.search-dishes {
  margin: 0 auto;
  width: 80%;
}
.metadata {
  margin: 1rem 2rem 0 2rem;
  display: flex;
  justify-content: space-between;
}
.dish-results {
  padding: 0;
  height: 50%;
  width: 50%;
  margin: 2rem auto;
}
.scrollbar {
  max-height: 30rem;
  overflow-y: scroll;
}
.direction-wrapper {
  margin: 1rem 2rem 0 2rem;
  display: flex;
  justify-content: space-between;
}
.content {
  margin-left: 1rem;
}
.name {
  position: absolute;
  margin-left: 0.5rem;
  bottom: 0.8rem;
}
.card-image {
  height: auto;
  width: auto;
}
</style>