<script setup>
import CoursItem from '../Courses/CoursItem.vue';
import {ref,onMounted  } from 'vue';
import axios from 'axios';
const products = ref([])

onMounted (() => {
    axios
      .get('http://127.0.0.1:8000/api/product')
      .then(res => products.value=res.data)
    
  console.log(products);
})
</script>
<template>
<div className="container my-3">
    <div class="container " >
        <div class="row "   >
<div class="col-4" v-for="product in products">
    <CoursItem key="product.id" :product="product" />
</div>
        </div>
    </div>
</div>
</template>



<style>

</style>