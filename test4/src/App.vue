<template>
  <div id="app">
    <Header /> <!-- TODO: parameterize header message !-->
    <ElementList v-bind:elements="elements"/> <!-- TODO: pass data !-->
  </div>
</template>

<script>
import json from './assets/data.json'
import Header from './components/Header.vue'
import ElementList from './components/ElementList.vue'

export default {
  name: 'App',
  components: {
    Header,
    ElementList
  },
  data() {
    return {
      elements: json,
    }
  },

  beforeCreate() {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
