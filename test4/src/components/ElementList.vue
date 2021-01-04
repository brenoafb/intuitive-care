<template>
  <div>
    <input type="text" v-model="searchQuery" @change="updateSearch" size="48" placeholder="Busca">
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
      const options = { caseSensitive: false, sort: true };
      const searcher = new FuzzySearch(this.elements, Object.keys(this.elements[0]), options);
      const results = searcher.search(this.searchQuery);
      return results;
    }
  }
}
</script>
