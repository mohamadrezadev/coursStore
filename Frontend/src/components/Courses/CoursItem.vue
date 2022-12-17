<template>
  <div className="col-lg-4 col-md-6 col-sm-12" >
    <div className="card custom-card mb-3" >
      <div className="sub-layer">
        <img
          src="images/bootstrap.jpg"
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
        <a href="course.html" className="card-link">آموزش جامع Bootstrap 4</a>
        <p className="text-justify card-text vazir font-14 mt-3">
          لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده
          از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و
          سطرآنچنان که لازم است.
        </p>
      </div>
      <div className="card-footer">
        <span className="badge badge-primary badge-pill pt-1">60%</span>
        <div className="float-left">
          <del className="text-muted font-13">120.000 تومان</del>
          <small className="text-success mr-2">75.000 تومان</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props=defineProps(["product"])
// const users =ref([])
//     function GetUsers(){
//         fetch("https://jsonplaceholder.typicode.com/users")
//         .then(response=>response.json())
//         .then(data=>users.value=data)
//     }
//     GetUsers()
</script>

<style>

</style>