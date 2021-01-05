<template>
  <div>
    <!-- <input type="text" v-model="searchQuery" @change="updateSearch" size="48" placeholder="Busca"> !-->
    <input type="text" v-model="searchQuery" size="48" placeholder="Busca">
    <button type="button" @click="fetchData">Buscar</button>
    <div v-for="element in elements" v-bind:key="element.id">
      <Element v-bind:element="element"/>
    </div>
  </div>
</template>

<script>

import Element from './Element.vue';
import axios from 'axios';

const API_URL = 'http://localhost:3000'; 

export default {
  name: 'ElementList',
  props: [],
  components: {
    Element
  },
  methods: {

    fetchData() {        
      console.log("Fetching data");
      let url = API_URL;
      if (this.searchQuery) {
        console.log(`searchQuery: ${this.searchQuery}`);
        url += `/?search=${this.searchQuery}`;
      }
      axios.get(url)
        .then(response => {
          this.elements = JSON.parse(response.data);
        })
        .catch(error => console.error(error));
    }
  },

  created() {
    this.fetchData()
  },

  data() {
    return {
      searchQuery: "",
      elements: []
    }
  },

  computed: {
  }
}
</script>
