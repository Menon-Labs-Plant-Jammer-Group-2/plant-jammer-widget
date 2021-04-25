<template>
  <div :class="backgroundDark ? 'dark-background' :''">
    <div v-if="!finishedRecipe && !failed" class="title is-3">Hang on, we're generating your recipe!</div>
    <div
      v-else-if="failed"
      class="title is-3"
    >Sorry we have a bug :( or the requested recipe made us time out</div>
    <div v-else>
      <div class="img-wrapper">
        <img class="img" :src="image" alt="placeholder" />
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
          v-for="(ingredient,index) in allIngredients['measurements']"
          :key="ingredient['ingredient']['name']"
        >
          <li
            class="ingredients-list"
          >{{ingredient['grams']!==undefined ? `${ingredient['grams']}g`:''}} {{ingredient['ingredient']['name']}}</li>
          <button
            v-if="ingredient['substitutes'] && ingredient['substitutes']['substitutes'].length>0"
            @click="changeBackground(ingredient['ingredient']['name'])"
            class="substitute button is-white is-small"
          >Substitute</button>

          <!-- MODAL FOR SUBSTITUTES -->
          <div
            v-if="substituteModal ===ingredient['ingredient']['name']"
            class="box is-active substitute-modal"
          >
            <div>
              <div class="header-modal">
                <div>
                  <div class="substitute-text">Substitute {{ingredient['ingredient']['name']}} for:</div>
                  <div class="substitute-button-wrapper">
                    <button
                      class="button substitute-button is-white"
                      v-for="substitute in ingredient['substitutes']['substitutes'].slice(0,3)"
                      :key="substitute['name']"
                      @click="substituteThis(ingredient['ingredient']['name'],substitute['name'])"
                    >{{substitute['name']}}</button>
                    <button
                      @click="removeIngredient(ingredient['ingredient']['name'],index)"
                      class="button is-rounded remove"
                    >REMOVE INGREDIENT</button>
                  </div>
                </div>
                <div class="delete-wrapper">
                  <button @click="undoBackground()" class="delete delete-modal"></button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- ENDS -->

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
import NProgress from "nprogress";
export default {
  name: "Step3",
  components: {},
  props: {
    chosen: Array,
    step: Number,
    selectedDish: String,
    image: String
  },
  data() {
    return {
      dishInfo: {},
      finishedRecipe: false,
      substituteModal: "",
      substituteIngredients: [],
      userChosen: [],
      failed: false,
      backgroundDark: false,
      tempChosen: JSON.parse(JSON.stringify(this.chosen))
    };
  },
  methods: {
    async getIngredients() {
      let url_ingredients = `https://menon-labs-api.xyz/all_ingredients/${this.selectedDish}`;
      this.userChosen = JSON.parse(JSON.stringify(this.tempChosen));
      try {
        const response = await axios.get(url_ingredients);
        let count = 0;
        let data = response.data["data"]["dishes"]; // if dishes is null that means there's an error object, most common culprit is that request timed out
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
            // removing duplicates
            let newChosenSet = new Set([
              ...JSON.parse(JSON.stringify(this.tempChosen)),
              ...newChosen
            ]);
            newChosen = [...newChosenSet];
            this.tempChosen = newChosen;
            await this.getRecipe();
            break;
          }
          count += 1;
        }
      } catch (err) {
        this.failed = true;
        console.log(err);
      }
    },
    async getRecipe() {
      let url = `https://menon-labs-api.xyz/recipe/?dish=${this.selectedDish}&`;
      let temp = this.substituteIngredients["ingredient"];

      // suggested ingredients
      for (let ingredient of temp) {
        url += `id=${parseInt(ingredient["id"])}&`;
      }
      // user chosen ingredients
      console.log(this.userChosen);
      for (let ingredient of this.userChosen) {
        url += `chosen=${ingredient}&`;
      }

      url = url.slice(0, url.length - 1); // to remove the extra & since that would mess with our backend
      console.log(url);
      try {
        const response = await axios.get(url);
        let count = 0;
        let data = response.data["data"]["dishes"];
        for (let dish of data) {
          console.log(dish);
          if (this.selectedDish === dish["name"]) {
            this.dishInfo = {
              name: data[count]["name"],
              mandatory: data[count]["mandatoryIngredients"],
              time: data[count]["estimatedPreparationTime"],
              servingName: data[count]["serving"]["name"],
              servingAmount: data[count]["serving"]["amount"],
              measurements: data[count]["ratio"]["volumes"],
              instructions: data[count]["blueprint"]["instructions"]
            };
            console.log(this.dishInfo);
            break;
          }
          count += 1;
        }

        this.finishedRecipe = true;
      } catch (error) {
        this.failed = true;
        console.log(error);
      }
    },
    changeBackground(name) {
      this.substituteModal = name;
      this.backgroundDark = true;
    },
    undoBackground() {
      this.substituteModal = "";
      this.backgroundDark = false;
    },
    removeIngredient(remove) {
      // removes the measurements
      console.log(remove);
      console.log(this.dishInfo["measurements"]);
      this.dishInfo["measurements"] = this.dishInfo["measurements"].filter(
        ingredient => ingredient["ingredient"]["name"] !== remove
      );
      console.log(this.dishInfo["measurements"]);
      // removes the ingredient that we wanted to remove substitutes'
      this.substituteIngredients["ingredient"] = this.substituteIngredients[
        "ingredient"
      ].filter(ingredient => ingredient["name"] !== remove);
      this.undoBackground();
    },
    substituteThis(chosenIngredient, substitute) {
      // replaces substitutes in the list of original ingredients to be displayed
      this.tempChosen = this.tempChosen.map(chose =>
        chose === chosenIngredient ? substitute : chose
      );
      this.dishInfo["measurements"] = this.dishInfo["measurements"].map(
        chose => {
          if (chose["ingredient"]["name"] === chosenIngredient) {
            chose["ingredient"]["name"] = substitute;
          }
          return chose;
        }
      );

      let tempSubstitutes = JSON.parse(
        JSON.stringify(this.substituteIngredients["ingredient"])
      ); // so we can work with this.substituteIngredients, otherwise we get an undefined error
      console.log(tempSubstitutes);

      // gets the original ingredient into the list of substitutes now
      this.substituteIngredients["ingredient"] = tempSubstitutes.map(
        ingredient => {
          if (ingredient["name"] === chosenIngredient) {
            let temp = ingredient["name"];
            ingredient["name"] = substitute;
            ingredient["substitutes"] = ingredient["substitutes"].map(item =>
              item["name"] === substitute ? { name: temp } : item
            );
            console.log(JSON.stringify(ingredient["substitutes"]));
          }
          return ingredient;
        }
      );
      this.undoBackground();
    }
  },
  async created() {
    NProgress.start();
    this.getIngredients();
    NProgress.done();
  },
  computed: {
    // for this computed property we combine the subsitutes with the info of the dishes into one object
    // which we use to render the data in the template tag, also makes sure that measurements and
    // substitutes are in sync with the name of the ingredient
    allIngredients: function() {
      let temp = JSON.parse(JSON.stringify(this.dishInfo));
      let tempSubstitutes = JSON.parse(
        JSON.stringify(this.substituteIngredients)
      );
      for (let substitutes of tempSubstitutes["ingredient"]) {
        for (let [index, dish] of temp["measurements"].entries()) {
          if (substitutes["name"] === dish["ingredient"]["name"]) {
            temp["measurements"][index]["substitutes"] = substitutes;
          }
        }
      }
      console.log(temp);

      return temp;
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
.dark-background {
  background: rgba(94, 97, 93, 0.3);
  /* opacity: 0.6; */
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
.substitute-button {
  background: inherit;
  color: #2d5d4c;
}
.substitute-button:hover {
  background: grey;
}
.substitute-button:focus {
  background: green;
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
.remove {
  background: #459071;
  color: white;
  font-family: Bebas Neue;
  text-align: center;
  font-size: 1.5rem;
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
  justify-content: space-around;
  align-items: flex-start;
}
.substitute-text {
  margin-top: 5%;
  text-align: center;
  font-size: 1rem;
  /* Color 1 */
  font-weight: 600;
  color: #2d5d4c;
}
.substitute-button-wrapper {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}
.delete-wrapper {
  margin-top: 0.5rem;
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