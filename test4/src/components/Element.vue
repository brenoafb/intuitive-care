<template>
  <div class="item">
    <p>{{element['Raz�o Social']}} {{element['CNPJ']}}</p>
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
    padding: 10px;
    border-bottom: 1px #ccc dotted;
  }

  .is-highlighted {
    background: #f6f6f6;
    text-decoration: line-through;
  }

  .del {
    background: #ff0000;
    color: #fff;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
  }

</style>
