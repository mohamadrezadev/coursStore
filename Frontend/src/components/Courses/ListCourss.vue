<script setup>
import CoursItem from "../Courses/CoursItem.vue";
import { ref, onMounted } from "vue";
import axios from "axios";
const products = ref([]);

onMounted(() => {
  axios
    .get("http://127.0.0.1:8000/api/product")
    .then((res) => (products.value = res.data));

  console.log(products);
});
</script>
<template>
  <div class="container my-3">
    <div class="container">
      <div class="row">
        <div v-for="(product) in products" class="col-4" :key="product.id" >
          <CoursItem  :product="product" />
        </div>
      </div>
    </div>
  </div>
</template>



<style>
</style>