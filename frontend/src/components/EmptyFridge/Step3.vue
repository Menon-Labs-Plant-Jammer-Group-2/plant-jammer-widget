<template>
  <div>
    <p>Hello</p>
    <!-- <div class="img-wrapper"><img :src=""</div> -->
    <div v-if="!finished" class="title is-3">Hang on, we're generating your recipe!</div>
    <div v-else>
      <div class="img-wrapper">
        <img class="img" :src="dishInfo['image']" />
      </div>
      <div class="title is-2">{{dishInfo['name']}}</div>
    </div>
    <div class="direction-wrapper">
      <div class="back-wrapper">
        <button @click="$emit('update:step',1)" class="next button is-success">
          <span class="icon is-small">
            <i class="fas fa-arrow-left"></i>
          </span>
          <span>Back</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Step3",
  components: {},
  props: {
    chosen: Array,
    step: Number,
    selectedDish: String
  },
  data() {
    return {
      dishInfo: {},
      finished: false
    };
  },
  async mounted() {
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
        let count = 0;
        let data = response.data["data"]["dishes"];
        for (let dish of data) {
          if (self.selectedDish === dish["name"]) {
            self.dishInfo = {
              name: data[count]["name"],
              mandatory: data[count]["mandatoryIngredients"],
              time: data[count]["estimatedPreparationTime"],
              image: data[count]["image"]["url"],
              servingName: data[count]["serving"]["name"],
              servingAmount: data[count]["serving"]["amount"],
              measurements: data[count]["ratio"]["volumes"],
              instructions: data[count]["blueprint"]["instructions"]
            };
          }
          count += 1;
        }

        self.finished = true;
      })
      .catch(function(error) {
        console.log(error);
      });
  }
};
</script>

<style scoped>
.back-wrapper {
  display: flex;
  justify-content: flex-start;
  margin-top: 1rem;
  margin-left: 2rem;
}
.img-wrapper {
  height: 50%;
}
.img {
  height: auto;
  width: 100%;
  max-height: 20rem;
}
</style>