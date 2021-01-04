<template>
  <div>
    <h2> List </h2>
    <input type="text" v-model="searchQuery" @change="updateSearch">
    <div v-for="element in filteredElements" v-bind:key="element.id">
      <Element v-bind:element="element"/>
      <!-- <p>{{element.id}} {{element.description}}</p> !-->
    </div>
  </div>
</template>

<script>

import Element from './Element.vue'
import FuzzySearch from 'fuzzy-search';

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
      searchQuery: "",
    }
  },

  computed: {
    filteredElements: function() {
      const searcher = new FuzzySearch(this.elements, Object.keys(this.elements[0]));
      const results = searcher.search(this.searchQuery);
      return results;
    }
  }
}
</script>
