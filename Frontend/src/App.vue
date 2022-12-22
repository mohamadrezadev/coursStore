<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Footer from './components/Footer/Footer.vue';
import Header from './components/Headers/Header.vue';
import 'vue3-toastify/dist/index.css';

</script>

<template>

<div class="">
  <Header/>
  <RouterView />
  <Footer/>
</div>
</template>
<style scoped>

</style>