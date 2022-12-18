<script setup>
import CoursItem from '../Courses/CoursItem.vue';
import {ref} from 'vue';

const products =ref([])
    function Getproduct(){
        fetch('https://fakestoreapi.com/products/1')
                .then(res=>res.json())
                .then(data=>products.value=data)
                .then(json=>console.log(json))

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