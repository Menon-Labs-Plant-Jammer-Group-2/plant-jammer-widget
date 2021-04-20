<template>
  <div>
    <div v-if="!finished" class="title is-3">Hang on, we're generating your recipe!</div>
    <div v-else>
      <div class="img-wrapper">
        <img class="img" :src="dishInfo['image']" />
      </div>

      <div class="header">
        <div class="title is-2">{{dishInfo['name']}}</div>
        <div class="icon-wrapper">
          <i class="fas fa-share-alt"></i>
        </div>
        <div class="icon-wrapper">
          <i class="fas fa-download"></i>
        </div>
      </div>

      <div class="metadata-recipe">
        <div class="time-wrapper">
          <div class="time title is-4">Time</div>
          <div class="minutes">{{dishInfo['time']}} mins</div>
        </div>
        <div class="line">&#124;</div>
        <div class="required-wrapper">
          <div class="required title is-4">Required</div>
          <div v-if="dishInfo['mandatory'].length > 0">
            <li
              class="mandatory-list"
              v-for="mandatory in dishInfo['mandatory']"
              :key="mandatory['name']"
            >{{mandatory["name"]}}</li>
          </div>
          <div v-else>None</div>
        </div>
      </div>

      <div class="ingredients">
        <div class="ing title is-4">Ingredients</div>
        <div
          class="ingredients-container"
          v-for="ingredient in allIngredients"
          :key="ingredient['name']"
        >
          <li
            class="ingredients-list"
          >{{ingredient['measurement']!==undefined ? `${ingredient['measurement']['grams']}g`:''}} {{ingredient['name']}}</li>
          <button
            @click="substituteModal = true"
            class="substitute button is-white is-small"
          >Substitute</button>
          <div v-if="substituteModal" class="modal is-active substitute-modal">
            <div class="modal-background"></div>
            <div class="modal-card">
              <section class="modal-card-body">We will display substitutable ingredients here</section>
            </div>
            <button @click="substituteModal = false" class="delete delete-modal"></button>
          </div>
        </div>
      </div>

      <div class="instructions">
        <div class="ins title is-4">Steps</div>
        <div class="instructions-list-wrapper">
          <li
            class="instructions-list"
            v-for="(step,index) in dishInfo['instructions']"
            :key="step['text']"
          >{{index+1}}. {{step['text']}}</li>
        </div>
      </div>
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
      finished: false,
      substituteModal: false
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
  },
  computed: {
    allIngredients: function() {
      let newChosen = JSON.parse(JSON.stringify(this.chosen)).sort(
        (a, b) => (a > b) - (a < b)
      ); // we're sorting since we get volumes from the api alphabetically and since we
      // merge that with the ingredients we selected, the measurements and ingredients wouldn't
      // be in sync
      let newDishInfo = this.dishInfo.mandatory.map(
        mandatory => mandatory["name"]
      );
      let mergedIngredients = [...newChosen, ...newDishInfo];
      let ingredientsSet = new Set(mergedIngredients); // for duplicate ingredients

      let ingredientsName = Array.from(ingredientsSet);
      let finalIngredients = ingredientsName.map((ingredient, i) => ({
        name: ingredient,
        measurement: this.dishInfo["measurements"][i]
      }));
      return finalIngredients;
    }
  }
};
</script>

<style scoped>
.header {
  display: flex;
  margin: 0 auto;
  justify-content: center;
  align-items: center;
}
.icon-wrapper {
  margin-top: 0.8rem;
  margin-left: 2rem;
  font-size: 1.5rem;
}
.metadata-recipe {
  display: flex;
  justify-content: space-evenly;
  align-items: flex-start;
}
.time-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.ingredients {
  width: 80%;
  margin: 0 auto;
}
.required-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.mandatory-list {
  list-style-type: none;
  margin-left: 0.8rem;
  text-align: center;
}
.ingredients-list {
  list-style-type: none;
}
.ingredients-container {
  border-top: 1px solid #e2f2d0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 2.5rem;
}
.time {
  margin: 0;
}
.required {
  margin: 0;
}
.line {
  font-size: 5rem;
  color: grey;
  font-weight: 100;
}
.ing {
  margin: 0;
  text-align: left;
  margin-bottom: 0.5rem;
}
.ins {
  margin: 0;
  text-align: left;
  margin-bottom: 0.5rem;
}
.instructions {
  width: 80%;
  margin: 0 auto;
}

.instructions-list {
  list-style-type: none;
  width: 95%;
  margin: 0 auto;
}
.instructions-list-wrapper {
  border-top: 1px solid #e2f2d0;
}
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
.substitute-modal {
  height: 10%;
  bottom: auto;
  width: 50%;
  top: 50%;
  left: 25%;
  right: 25%;
  background: white;
  z-index: 20;
}
.modal-background {
  background-color: white;
}
.modal-card {
  height: 100%;
}
.delete-modal {
  left: 40%;
  top: -70%;
}
</style>