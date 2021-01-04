<template>
  <div id="app">
    <Header /> <!-- TODO: parameterize header message !-->
    <ElementList v-bind:elements="elements"/> <!-- TODO: pass data !-->
  </div>
</template>

<script>
import Header from './components/Header.vue'
import ElementList from './components/ElementList.vue'

export default {
  name: 'App',
  components: {
    Header,
    ElementList
  },
  data() {
    // TODO read csv
    return {
      elements: [
        {
          id: 1,
          description: "Componente Organizacional"
        },
        {
          id: 2,
          description: "Componente de Conteúdo e Estrutura"
        },
        {
          id: 3,
          description: "Componente de Representação de Conceitos em Saúde"
        },
      ]
    }
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
