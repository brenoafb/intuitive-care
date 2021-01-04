<template>
  <div>
    <h2> List </h2>
    <input type="text" v-model="searchQuery" @change="updateSearch">
    <div v-for="element in elements" v-bind:key="element.id">
      <Element v-bind:element="element"/>
      <!-- <p>{{element.id}} {{element.description}}</p> !-->
    </div>
  </div>
</template>

<script>

import Element from './Element.vue'

export default {
  name: 'ElementList',
  props: ["elements"],
  components: {
    Element
  },
  methods: {
    updateSearch() {
      console.log(this.searchQuery)
    }
  },

  data() {
    return {
      searchQuery: ""
    }
  }
}
</script>
