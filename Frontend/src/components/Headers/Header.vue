<script setup>
import Navbar from './Navbar.vue';

</script>
<template>
    <header class="bg-white">
        <div class="container">
            <div class="row py-3">

                <div class="d-none d-lg-block col-lg-2">
                    <img src="images/minlogo.jpg" alt="EasyLearn" title="EasyLearn" class="img-fluid"/>
                </div>

                <div class="d-none d-lg-flex col-lg-6 align-items-center search-box">
                    <form action="" method="">
                        <div class="input-group">
                            <input type="search" name="" class="form-control rounded-pill" placeholder="عنوان مورد نظر خود را جستجو کنید ..."/>
                            <div class="input-group-append">
                                <button type="submit" class="btn btn-info rounded-pill font-13">جستجو</button>
                            </div>
                        </div>
                    </form>
                </div>

                <div class="d-none d-lg-flex col-lg-4 align-items-center justify-content-end">
                    <a href="#" class="cart mt-2 ml-2 dropdown" data-toggle="dropdown"><span class="badge badge-info badge-pill">2</span><i class="fa fa-shopping-basket"></i>
                        <div class="dropdown-menu dropdown-cart mt-3">
                            <ul class="list-unstyled">
                                <li><img src="images/bootstrap.jpg" class="m-1 ml-3"/>
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">آموزش جامع Bootstrap 4 (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><img src="images/php-security-2.png" class="m-1 ml-3"/>
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">آموزش امنیت در PHP (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li>
                                    <router-link to="/Panel" class="btn btn-info m-1 ml-3 font-12">
                                        <p class="text-dark">
                                            پرداخت
                                        </p>
                                    </router-link>
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">قیمت کل : 128.000 تومان</small>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </a>
                    <router-link to="/register"  class="btn btn-outline-info font-13 vazir-med-fa" active-class="text-secondary">  ثبت نام  <i class="fa fa-user-plus pl-1">
                       </i> </router-link>
                    <router-link to="/login"  class="btn btn-info font-13 vazir-med-fa mx-2 " active-class="text-dark">ورود</router-link>
                </div>

            </div>

            <div class="row">
                <div class="col-12 d-flex d-lg-none justify-content-center">
                    <img src="images/logo.jpg" alt="Easylearn" />
                </div>

                <div class="col-12 d-flex d-lg-none justify-content-center mb-4 mobile-header">
                    <a href="sign-up.html" class="border-left ml-3"><i class="fa fa-user-plus ml-3"></i></a>
                    <a href="login.html" class="border-left ml-3"><i class="fa fa-lock ml-3"></i></a>
                    <a href="teach.html" class="border-left ml-3"><i class="fa fa-graduation-cap ml-3"></i></a>
                    <a href="#" class="border-left ml-3 dropdown" data-toggle="dropdown"><span class="badge badge-info badge-pill">2</span><i class="fa fa-shopping-basket ml-3"></i>
                        <div class="dropdown-menu  dropdown-cart mt-3 mx-5">
                            <ul class="list-unstyled">
                                <li><img src="images/bootstrap.jpg" class="m-1 ml-3">
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">آموزش جامع Bootstrap 4 (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><img src="images/php-security-2.png" class="m-1 ml-3"/>
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">آموزش امنیت در PHP (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><button class="btn btn-info m-1 ml-3 font-12">پرداخت</button>
                                    <div class="float-right">
                                        <small class=" mt-3 mr-2 d-block">قیمت کل : 128.000 تومان</small>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </a>
                    <a href="#" data-toggle="collapse"><i class="fa fa-search"></i></a>
                </div>

                <div id="search" class=" d-lg-none col-10 mx-auto collapse mb-4 justify-content-center">
                    <form action="" method="">
                        <div class="input-group">
                            <input type="search" name="" class="form-control rounded-pill" placeholder="عنوان مورد نظر خود را جستجو کنید ...">
                            <div class="input-group-append">
                                <button type="submit" class="btn btn-info rounded-pill font-13">جستجو</button>
                            </div>
                        </div>
                    </form>
                </div>

            </div>
        </div>
        <Navbar/>
    </header>
</template>



<style>

</style>