<template>
  <div>
    <div v-if="searchData.length!=0">
      <div class="search-dishes">
        <p class="control has-icons-right">
          <input class="input is-rounded" type="text" v-model="searchQuery" placeholder="Search" />
          <span class="icon is-small is-right">
            <i class="fas fa-search"></i>
          </span>
        </p>
      </div>

      <div class="metadata">
        <button @click="$emit('update:filterClicked',true)" class="filter-button button is-white">
          <span class="icon">
            <i class="fas fa-sliders-h"></i>
          </span>
          <span>FILTER</span>
        </button>
        <button
          @click="$emit('update:fridgeClicked',true)"
          class="fridge-button button is-white"
        >YOUR FRIDGE</button>
      </div>
      <div>
        <h1>We found {{searchData.length}} recipes</h1>
        <h1 v-if="selectedClicked">You've selected {{selectedDish}}</h1>
        <h1>Click on a recipe to select it!</h1>
        <div class="scrollbar">
          <div
            class="dish-results"
            v-for="(dish,index) in (timeClicked ?  filteredDishesTime : filteredDishes)"
            :key="dish['properties']['name']"
          >
            <div
              @mouseover="showDescription = index"
              @mouseleave="showDescription = -1"
              @click="selected(dish)"
              class="card"
            >
              <div class="card-image">
                <img class="dish-image" :src="dish['properties']['image']" alt="Placeholder image" />
                <div
                  v-if="showDescription===index"
                  class="dish-description"
                >{{dish['properties']['description']}}</div>
                <div class="name">
                  <p class="dish-name title is-4">{{dish["properties"]["name"]}}</p>
                </div>
              </div>
              <div class="content">
                <div>
                  Time
                  <div class="time">{{dish['properties']["time"]}} minutes</div>
                </div>
                <div>
                  Required
                  <div
                    v-if="dish['properties']['required']"
                  >{{dish['properties']['required'].join(", ").length>0? dish['properties']['required'].join(", "): "None"}}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else-if="finished===false">
      <h1 class="title">Hang on! We're fetching some recipes :)</h1>
    </div>
    <div v-else-if="searchData.length===0">
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
      <div v-if="selectedClicked" class="next-wrapper">
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
import NProgress from "nprogress";
export default {
  name: "Step2",
  components: {},
  props: {
    step: Number,
    chosen: Array,
    fridgeClicked: Boolean,
    searchData: Array,
    filterClicked: Boolean,
    timeClicked: Boolean,
    filteredTimes: Array,
    selectedDish: String,
    suggestedNames: Set,
    image: String
  },
  data() {
    return {
      searchQuery: "",
      finished: false,
      selectedClicked: false,
      showDescription: -1
    };
  },
  methods: {
    selected: function(dish) {
      this.$emit("update:image", dish["properties"]["image"]);
      this.$emit("update:selectedDish", dish["properties"]["name"]);
      this.selectedClicked = true;
    },
    filterSearch: function(data) {
      return data.filter(dish => {
        let temp = JSON.parse(JSON.stringify(dish));
        temp = temp["properties"]["name"];
        return temp.toLowerCase().indexOf(this.searchQuery.toLowerCase()) >= 0;
      });
    },
    async populateSearchField() {
      let url = "http://127.0.0.1:8000/recipe/?";
      let selected = JSON.parse(JSON.stringify(this.chosen));

      for (let ingredient of selected) {
        ingredient = ingredient.split(" ").join("");
        url += `keywords=${ingredient}&`;
      }
      url = url.slice(0, url.length - 1); // to remove the extra & since that would mess with our backend
      try {
        const response = await axios.get(url);
        let tempObj = [];
        let data = response.data["data"]["dishes"];
        for (let dish of data) {
          let properties = {
            properties: {
              name: dish["name"],
              time: dish["estimatedPreparationTime"],
              image: dish["image"]["url"],
              required: dish["mandatoryIngredients"].map(
                ingredient => ingredient["name"]
              ),
              description: dish["description"]
            }
          };
          if (!this.suggestedNames.has(dish["name"])) {
            tempObj.push(properties);
            this.suggestedNames.add(dish["name"]);
          }
        }
        if (tempObj.length !== 0) this.$emit("update:searchData", tempObj);
        this.finished = true;
        NProgress.done();
      } catch (error) {
        console.log(error);
      }
    }
  },
  async created() {
    /* Here we just get the generated recipes of the ingredients that we had 
    from step 1  */
    NProgress.start();
    this.populateSearchField();
  },
  computed: {
    filteredDishes: function() {
      return this.filterSearch(this.searchData);
    },
    filteredDishesTime: function() {
      return this.filterSearch(this.filteredTimes);
    }
  }
};
</script>

<style scoped>
.search-dishes {
  margin: 0 auto;
  width: 80%;
}
input {
  color: #2d5d4c;
  border: 1px solid #e2f7cb;
}
::placeholder {
  color: #2d5d4c;
}
.metadata {
  margin: 1rem 2rem 0 2rem;
  display: flex;
  justify-content: space-between;
}
.direction-wrapper {
  margin: 1rem 2rem 0 2rem;
  display: flex;
  justify-content: space-between;
}
.filter-button {
  font-family: "Bebas Neue";
  font-size: 1.5rem;
  color: #2d5d4c;
}
.fridge-button {
  font-family: "Bebas Neue";
  font-size: 1.5rem;
  color: #2d5d4c;
}
.fa-search {
  color: #459071;
}
.scrollbar {
  max-height: 30rem;
  overflow-y: scroll;
}
.card-image {
  height: auto;
  width: auto;
}
.name {
  position: absolute;
  margin-left: 0.5rem;
  bottom: 0.8rem;
}
.content {
  margin: 0 1rem;
  color: white;
  display: flex;
  justify-content: space-between;
}
.card {
  border-radius: 10px;
  background: #58977d;
}
.dish-name {
  font-family: Bebas Neue;
  color: white;
  font-size: 2rem;
  text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.dish-image {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  width: 100%;
  position: relative;
}
.dish-description {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  padding: 1rem;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0%;
  color: white;
  background: #2d5d4c;
}
.dish-results {
  padding: 0;
  height: 50%;
  width: 50%;
  margin: 2rem auto;
}
.filter-box {
  width: 100%;
  height: 100%;
  z-index: 1;
}
</style>