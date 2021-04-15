<template>
  <div class="app">
    <div class="box">
      <div class="title">Plant Jammer</div>

      <home />
      <div class="parent" v-for="(cuisine,index1) in cuisines" :key="cuisine">
        <h1 class="subt title is-4">{{cuisine}}</h1>
        <div class="level img-holder">
          <figure v-for="(url,index) in images[index1]" :key="index" class="image is-128x128">
            <img v-if="order[index1]===cuisine" :src="url" />
          </figure>
        </div>
      </div>
      <div class="footer-app">
        <button class="button bottom">
          <i class="fas fa-home" />
        </button>
        <button class="button bottom">
          <i class="fas fa-shopping-cart" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Home from "./components/Home/Home.vue";
import axios from "axios";
export default {
  name: "App",
  components: { Home },

  data() {
    return {
      cuisines: ["Italian", "Indian", "Vegan"],
      images: [],
      order: [],
      loaded: false
    };
  },
  methods: {},
  async mounted() {
    for (let name of this.cuisines) {
      let self = this;
      console.log(this.images);
      axios
        .get(`http://127.0.0.1:8000/dishes/${name}`)
        .then(function(response) {
          let tempArr = [];
          for (let i = 0; i < 4; ++i) {
            tempArr.push(response.data["data"]["dishes"][i]["image"]["url"]);
          }
          self.order.push(name);
          self.images.push(tempArr);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
    this.loaded = true;
  }
  // computed: {

  // }
};
</script>

<style>
.app {
  margin-top: 5%;
}
.box {
  width: 50%;
  margin: 0 auto;
  padding: 0;
}
.title {
  padding-top: 2rem;
  text-align: center;
}
.wrapper {
  height: 30%;
}

.empty {
  margin: 0 auto;
  width: 70%;
  justify-content: center;
  align-items: center;
  height: 100%;
}
@media screen and (min-width: 769px), print .columns:not(.is-desktop) {
  display: none;
}
.fridge {
  font-size: 2rem;
}
.desc {
  font-size: 1rem;
  overflow-wrap: break-word;
}
.input {
  width: 35%;
  margin-top: 2%;
  margin-left: 60%;
}
.bottom {
  margin-top: 2rem;
  width: 50%;
  height: 90%;
}
.fas {
  font-size: 2rem;
}
.subt {
  margin-left: 2rem;
  text-align: left;
}
.image {
  display: inline-block;
}
.parent {
  padding: 0 2rem;
}
</style>
