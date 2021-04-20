<template>
  <div>
    <div class="parent" v-for="(cuisine,index1) in order" :key="cuisine">
      <h1 class="subt title is-4">{{cuisine}}</h1>
      <div class="level img-holder">
        <figure class="image is-128x128" v-for="(url,index) in images[index1]" :key="index">
          <img class="individuals" v-if="order[index1]===cuisine" :src="url" />
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Gallery",
  components: {},
  props: {
    state: Number
  },
  data() {
    return {
      cuisines: ["Italian", "Indian", "Vegan"],
      images: [],
      order: []
    };
  },
  async mounted() {
    // making sure that images are being rendered in the home screen from the server
    // it's very slow rn
    for (let name of this.cuisines) {
      let self = this;
      console.log(this.images);
      axios
        .get(`http://155.138.211.205/dishes/${name}`)
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
  }
};
</script>

<style scoped>
.subt {
  margin-left: 2rem;
  text-align: left;
}
.image {
  display: inline-block;
  margin: 0 0.5rem;
}
.parent {
  padding: 0 2rem;
}
.individuals {
  height: 100%;
}
</style>