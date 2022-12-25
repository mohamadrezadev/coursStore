<template>
  <div class="" >
    <div class="card custom-card mb-3" >
      <div class="sub-layer">
        <img
          :src="url+product.image"
          alt="bootstrap"
          class="img-fluid card-img-top"
        />
        <div class="over-layer">
          <a href="course.html" class="btn btn-primary"> مشاهده و خرید </a>
          <span class="badge badge-secondary badge-pill">
            50 <i class="fa fa-shopping-basket pr-1"></i
          ></span>
        </div>
      </div>

      <div class="card-body">
        <a href="course.html" class="card-link">{{ props.product.Name }}</a>
        <p class="text-justify card-text vazir font-14 mt-3">
          {{ props.product.description }}
        </p>
      </div>
      <div class="card-footer">
        <span class="badge badge-primary badge-pill pt-1">60%</span>
        <div class="float-left">
          <del class="text-muted font-13">120.000 تومان</del>
          <small class="text-success mr-2">{{props.product.price}}</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props=defineProps(["product"])
const url ="http://127.0.0.1:8000/"
</script>

<style>

</style>