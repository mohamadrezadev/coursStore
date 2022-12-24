<template>
  <TitleBox title=" جدیدترین دوره های آموزشی" />
  <div class="container my-3">
    <div class="row">
      <Course  />
      <Course />
      <Course />
    </div>
  </div>
</template>

<script setup>
import TitleBox from "../Title/TitleBox.vue";
import Course from "./Course.vue";
</script>

<style></style>
