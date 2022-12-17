<script setup>
import CoursItem from '../Courses/CoursItem.vue';
import {ref} from 'vue';
const products =ref([])
    function Getproduct(){
        fetch("https://jsonplaceholder.typicode.com/posts")
        .then(response=>response.json())
        .then(data=>products.value=data)
    }
Getproduct()
for (var product in products){
    console.log(product.title);
}
</script>
<template>
<div className="container my-3">
    <div className="row">
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
        <CoursItem/>
    </div>
</div>
</template>



<style>

</style>