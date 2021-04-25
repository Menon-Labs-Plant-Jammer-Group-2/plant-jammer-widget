<template>
  <div>
    <div class="parent-wrapper">
      <div class="parent" v-for="(cuisine,index) in cuisines" :key="cuisine">
        <h1 class="subt title is-4">{{cuisine}}</h1>
        <img class="individuals" :src="images[index]" />
      </div>
    </div>
  </div>
</template>

<script>
import Cookies from "../../../assets/cookies.jpeg";
import Muffins from "../../../assets/muffins.jpeg";
import Ratatouille from "../../../assets/roastzucchinipepper.jpeg";
import Soup from "../../../assets/sopa_calabaza.jpeg";
import Lasagna from "../../../assets/luke-johnson-inC_KZ5oZCI-unsplash.jpeg";
import Noodles from "../../../assets/vita-marija-murenaite-5Q_Edarv5zQ-unsplash.jpeg";
export default {
  name: "Gallery",
  components: {},
  props: {
    state: Number
  },
  data() {
    return {
      cuisines: [
        "Cookies",
        "Muffins",
        "Ratatouille",
        "Soup",
        "Lasagna",
        "Noodles"
      ],
      images: [Cookies, Muffins, Ratatouille, Soup, Lasagna, Noodles]
    };
  }
};
</script>

<style scoped>
.parent-wrapper {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding-bottom: 2rem;
}
.subt {
  z-index: 2;
  padding-left: 1rem;
  margin-left: 1rem;
  margin-bottom: 1rem;
  font-family: Bebas Neue;
  font-style: normal;
  font-weight: normal;
  letter-spacing: 0.05em;
  position: absolute;
  color: #f9f9f9;
}
.parent {
  position: relative;
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
  background: white;
  height: 15rem;
  width: 15rem;
  margin: 1rem 2rem;
}
.individuals {
  z-index: 1;
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 15px;
}
</style>