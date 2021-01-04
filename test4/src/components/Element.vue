<template>
  <div class="item">
    <h4>{{element['Raz�o Social']}}</h4>
    <ul>
      <li>{{element['Modalidade']}}</li>
      <li>{{element['Cidade']}} - {{element['UF']}}</li>
      <li>({{element['DDD']}}) {{element['Telefone']}}</li>
      <li>{{element['Representante']}}</li>
      <li>{{element['Endere�o eletr�nico']}}</li>
      <li>CEP: {{element['CEP']}}</li>
      <li>{{element['Logradouro']}}, {{element['Complemento']}}, {{element['N�mero']}}, {{element['Bairro']}}</li>
      <li>Registro ANS: {{element['Registro ANS']}} - {{element['Data Registro ANS']}}</li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Element',
  props: ["element"]
}
</script>

<style scoped>

  .item {
    background: #f4f4f4;
    padding: 3px;
    border-bottom: 1px #ccc dotted;
  }

  .is-highlighted {
    background: #f6f6f6;
    text-decoration: line-through;
  }

</style>
