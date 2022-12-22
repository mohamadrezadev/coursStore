<template>
  <div className="" >
    <div className="card custom-card mb-3" >
      <div className="sub-layer">
        <img
          :src="url+product.image"
          alt="bootstrap"
          className="img-fluid card-img-top"
        />
        <div className="over-layer">
          <a href="course.html" className="btn btn-primary"> مشاهده و خرید </a>
          <span className="badge badge-secondary badge-pill">
            50 <i className="fa fa-shopping-basket pr-1"></i
          ></span>
        </div>
      </div>

      <div className="card-body">
        <a href="course.html" className="card-link">{{ props.product.Name }}</a>
        <p className="text-justify card-text vazir font-14 mt-3">
          {{ props.product.description }}
        </p>
      </div>
      <div className="card-footer">
        <span className="badge badge-primary badge-pill pt-1">60%</span>
        <div className="float-left">
          <del className="text-muted font-13">120.000 تومان</del>
          <small className="text-success mr-2">{{props.product.price}}</small>
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