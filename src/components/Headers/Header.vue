<script setup>
import Navbar from './Navbar.vue';

</script>
<template>
    <header className="bg-white">
        <div className="container">
            <div className="row pb-3">

                <div className="d-none d-lg-block col-lg-2">
                    <img src="images/logo.jpg" alt="EasyLearn" title="EasyLearn" className="img-fluid"/>
                </div>

                <div className="d-none d-lg-flex col-lg-6 align-items-center search-box">
                    <form action="" method="">
                        <div className="input-group">
                            <input type="search" name="" className="form-control rounded-pill" placeholder="عنوان مورد نظر خود را جستجو کنید ..."/>
                            <div className="input-group-append">
                                <button type="submit" className="btn btn-info rounded-pill font-13">جستجو</button>
                            </div>
                        </div>
                    </form>
                </div>

                <div className="d-none d-lg-flex col-lg-4 align-items-center justify-content-end">
                    <a href="#" className="cart mt-2 ml-2 dropdown" data-toggle="dropdown"><span className="badge badge-info badge-pill">2</span><i className="fa fa-shopping-basket"></i>
                        <div className="dropdown-menu dropdown-cart mt-3">
                            <ul className="list-unstyled">
                                <li><img src="images/bootstrap.jpg" className="m-1 ml-3"/>
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">آموزش جامع Bootstrap 4 (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><img src="images/php-security-2.png" className="m-1 ml-3"/>
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">آموزش امنیت در PHP (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li>
                                    <router-link to="/Panel" className="btn btn-info m-1 ml-3 font-12">
                                        <p>
                                            پرداخت
                                        </p>
                                    </router-link>                            
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">قیمت کل : 128.000 تومان</small>
                                    </div>
                                </li>
                            </ul>
                        </div>  
                    </a>
                    <a href="" className="btn btn-outline-info font-13 vazir-med-fa"><i className="fa fa-user-plus pl-1"></i>ثبت نام</a>
                    <a href="" className="btn btn-info font-13 vazir-med-fa mx-2">ورود</a>
                </div>

            </div>

            <div className="row">
                <div className="col-12 d-flex d-lg-none justify-content-center">
                    <img src="images/logo.jpg" alt="Easylearn" />
                </div>

                <div className="col-12 d-flex d-lg-none justify-content-center mb-4 mobile-header">
                    <a href="sign-up.html" className="border-left ml-3"><i className="fa fa-user-plus ml-3"></i></a>
                    <a href="login.html" className="border-left ml-3"><i className="fa fa-lock ml-3"></i></a>
                    <a href="teach.html" className="border-left ml-3"><i className="fa fa-graduation-cap ml-3"></i></a>
                    <a href="#" className="border-left ml-3 dropdown" data-toggle="dropdown"><span className="badge badge-info badge-pill">2</span><i className="fa fa-shopping-basket ml-3"></i>
                        <div className="dropdown-menu  dropdown-cart mt-3 mx-5">
                            <ul className="list-unstyled">
                                <li><img src="images/bootstrap.jpg" className="m-1 ml-3">
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">آموزش جامع Bootstrap 4 (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><img src="images/php-security-2.png" className="m-1 ml-3"/>
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">آموزش امنیت در PHP (64.000 تومان)</small>
                                    </div>
                                </li>
                                <li><button className="btn btn-info m-1 ml-3 font-12">پرداخت</button>
                                    <div className="float-right">
                                        <small className=" mt-3 mr-2 d-block">قیمت کل : 128.000 تومان</small>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </a>
                    <a href="#search" data-toggle="collapse"><i className="fa fa-search"></i></a>
                </div>

                <div id="search" className=" d-lg-none col-10 mx-auto collapse mb-4 justify-content-center">
                    <form action="" method="">
                        <div className="input-group">
                            <input type="search" name="" className="form-control rounded-pill" placeholder="عنوان مورد نظر خود را جستجو کنید ...">
                            <div className="input-group-append">
                                <button type="submit" className="btn btn-info rounded-pill font-13">جستجو</button>
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