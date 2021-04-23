<template>
  <div>
    <div v-if="!finishedRecipe" class="title is-3">Hang on, we're generating your recipe!</div>
    <div v-else>
      <div class="img-wrapper">
        <img class="img" :src="dishInfo['image']" />
      </div>

      <div class="header">
        <div class="recipe-title title is-2">{{dishInfo['name']}}</div>
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
          v-for="(ingredient,index) in allIngredients"
          :key="ingredient['name']"
        >
          <li
            class="ingredients-list"
          >{{ingredient['measurement']!==undefined ? `${ingredient['measurement']['grams']}g`:''}} {{ingredient['name']}}</li>
          <button
            @click="substituteModal = index"
            class="substitute button is-white is-small"
          >Substitute</button>
          <div v-if="substituteModal===index" class="box is-active substitute-modal">
            <div class="header-modal">
              <div class="substitute-text">Substitute {{ingredient['name']}} for:</div>
              <div class="delete-wrapper">
                <button @click="substituteModal = -1" class="delete delete-modal"></button>
              </div>
            </div>
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
    selectedDish: String,
    callbackEmit: Function
  },
  data() {
    return {
      dishInfo: {},
      finishedRecipe: false,
      substituteModal: -1,
      substituteIngredients: []
    };
  },
  methods: {
    async getIngredients() {
      let url_ingredients = `http://127.0.0.1:8000/all_ingredients/${this.selectedDish}`;
      try {
        const response = await axios.get(url_ingredients);
        let count = 0;
        let data = response.data["data"]["dishes"];
        for (let dish of data) {
          if (this.selectedDish === dish["name"]) {
            this.substituteIngredients = {
              ingredient: data[count]["suggestedIngredients"]
            };
            let temp = JSON.parse(JSON.stringify(this.substituteIngredients));
            let newChosen = [];
            for (let ingredient of temp["ingredient"]) {
              newChosen.push(ingredient["name"]);
            }
            let newChosenSet = new Set([
              ...JSON.parse(JSON.stringify(this.chosen)),
              ...newChosen
            ]);
            newChosen = [...newChosenSet];
            console.log(newChosen);
            await this.callbackEmit(newChosen);
            this.getRecipe();
            // debugger; // eslint-disable-line no-debugger

            break;
          }
          count += 1;
        }
      } catch (err) {
        console.log(err);
      }
    },
    getRecipe() {
      let self = this;
      let url = `http://127.0.0.1:8000/recipes/?dish=${this.selectedDish}&`;
      let temp = this.substituteIngredients["ingredient"];
      // debugger; // eslint-disable-line no-debugger

      for (let ingredient of temp) {
        url += `id=${parseInt(ingredient["id"])}&`;
        console.log(url);
      }
      url = url.slice(0, url.length - 1); // to remove the extra & since that would mess with our backend
      console.log(url);
      // debugger; // eslint-disable-line no-debugger
      axios
        .get(url)
        .then(function(response) {
          // debugger; // eslint-disable-line no-debugger

          let count = 0;
          let data = response.data["data"]["dishes"];
          for (let dish of data) {
            console.log(dish);
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
              console.log(self.dishInfo);
              // debugger; // eslint-disable-line no-debugger
            }
            count += 1;
          }

          self.finishedRecipe = true;
        })
        .catch(function(error) {
          // debugger; // eslint-disable-line no-debugger

          console.log(error);
        });
    }
  },
  async mounted() {
    return this.getIngredients();
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
.banner {
  position: absolute;
  width: 70%;
  height: 2%;
  left: 4%;
  top: 50%;
  z-index: auto;
  background: #e2f7cb;
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
.recipe-title {
  font-family: Bebas Neue;
  padding-top: 1rem;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.08em;
  z-index: 4;
  /* Color 1 */

  color: #2d5d4c;
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
.minutes {
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.08em;
  color: #67b093;
}
.mandatory-list {
  list-style-type: none;
  margin-left: 0.8rem;
  text-align: center;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.08em;
  color: #67b093;
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
  color: #b1cbad;
  letter-spacing: 0.08em;
  font-style: normal;
  font-weight: normal;
}
.required {
  margin: 0;
  color: #b1cbad;
  letter-spacing: 0.08em;
  font-style: normal;
  font-weight: normal;
}
.line {
  font-size: 5rem;
  color: grey;
  font-weight: 100;
}
.ing {
  margin: 0;
  text-align: left;
  margin-bottom: 0.5rem !important;
}
.ins {
  margin: 0;
  text-align: left;
  margin-bottom: 0.5rem !important;
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
.header-modal {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
.substitute-text {
  margin-top: 5%;
  text-align: center;
  font-size: 1rem;
  /* Color 1 */
  font-weight: 600;
  color: #2d5d4c;
}
.delete-wrapper {
  padding-left: 30%;
}
.delete-modal {
  padding: 0 auto;
}
.substitute-modal {
  background: #f9f9f9;
  border: 1px solid #95ce8c;
  box-sizing: border-box;
  border-radius: 5px;
  position: absolute;
  z-index: 2;
  margin-left: 10%;
}
</style>