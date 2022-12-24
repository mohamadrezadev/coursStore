<script setup>

</script>
<template>
   <nav class="navbar navbar-expand-lg bg-white navbar-light shadow-sm sticky-top">

<div class="container">
    <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#mainmenu">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="mainmenu">
        <ul class="navbar-nav pr-0 custom-navbar font-14 text-center">
            <li class="nav-item ml-3 custom-nav-item"><router-link exact-active-class="text-info" to="/" class="nav-link" active-class="text-info"> صفحه اصلی</router-link></li>
            <li class="nav-item ml-3 dropdown custom-nav-item"><router-link to="/Courses"  class="nav-link  " active-class="text-info" >دوره های آموزشی</router-link>
            </li>
            <li class="nav-item ml-3 custom-nav-item"><router-link to="/blogs" class="nav-link" active-class="text-info">بلاگ</router-link></li>
            <li class="nav-item ml-3 custom-nav-item"><router-link to="/contact" class="nav-link" active-class="text-info">تماس با ما </router-link></li>
        </ul>
    </div>
</div>
</nav>
</template>



<style>

</style>