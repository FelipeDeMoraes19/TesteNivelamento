<template>
  <div>
    <input v-model="textoBusca" placeholder="Buscar operadora..." />
    <button @click="buscarOperadoras">Buscar</button>

    <ul>
      <li v-for="operadora in operadoras" :key="operadora.Registro_ANS">
        <strong>{{ operadora.Nome_Fantasia }}</strong> - {{ operadora.Cidade }}/{{ operadora.UF }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

interface Operadora {
  Registro_ANS: string
  Nome_Fantasia: string
  Cidade: string
  UF: string
}

const textoBusca = ref('')
const operadoras = ref<Operadora[]>([])

const buscarOperadoras = async () => {
  try {
    const response = await axios.get<Operadora[]>(`http://localhost:8000/buscar/?texto=${textoBusca.value}`)
    operadoras.value = response.data
  } catch (error) {
    console.error('Erro ao buscar operadoras:', error)
  }
}
</script>

<style scoped>
input {
  padding: 8px;
  width: 250px;
  margin-right: 8px;
}
button {
  padding: 8px;
}
</style>
