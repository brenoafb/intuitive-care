<template>
  <div id="app">
    <Header msg="Relação de Operadoras Ativas ANS" />
    <ElementList/>
  </div>
</template>

<script>
// import json from './assets/data.json'
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
      elements: []
    }
  },
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
