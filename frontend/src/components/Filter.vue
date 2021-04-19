<template>
  <div class="box filter-box">
    <div class="exit-wrapper">
      <button @click="$emit('update:filterClicked',false)" class="delete exit"></button>
    </div>
    <p class="filter-title title is-3">Your fridge</p>
    <div class="input-wrapper">
      <input class="input is-rounded" v-model="searchQuery" type="text" placeholder="Search" />
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
</template>

<script>
export default {
  name: "Fridge",
  props: {
    chosen: Array,
    fridgeClicked: Boolean
  },
  data() {
    return {
      searchQuery: ""
    };
  },
  methods: {
    removeIngredient: function(ingredient) {
      let newChosen = this.chosen.filter(item => item != ingredient);
      console.log(newChosen);
      this.$emit("update:chosen", newChosen);
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

.filter-box {
  position: absolute;
  z-index: 10;
  margin: 0 0 0 50%;
  height: 100%;
}
.input-wrapper {
  width: 80%;
  margin: 0 auto 2rem auto;
}
.item {
  display: flex;
  justify-content: center;
  align-items: center;
}
.item {
  text-align: center;
}
.delete-wrapper {
  margin: 0.3rem 0 0 0.2rem;
}
</style>