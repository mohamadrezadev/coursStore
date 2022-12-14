<script setup>

</script>
<template>
   <nav className="navbar navbar-expand-lg bg-white navbar-light shadow-sm sticky-top">

<div className="container">
    <button type="button" className="navbar-toggler" data-toggle="collapse" data-target="#mainmenu">
        <span className="navbar-toggler-icon"></span>
    </button>

    <div className="collapse navbar-collapse" id="mainmenu">
        <ul className="navbar-nav pr-0 custom-navbar font-14 text-center">
            <li className="nav-item ml-3 custom-nav-item"><router-link to="/" className="nav-link"> صفحه اصلی</router-link></li>
            <li className="nav-item ml-3 dropdown custom-nav-item"><router-link to="/Courss"  className="nav-link  " >دوره های آموزشی</router-link>
            </li>
            <li className="nav-item ml-3 custom-nav-item"><router-link to="/blogs" className="nav-link">بلاگ</router-link></li>
            <li className="nav-item ml-3 custom-nav-item"><router-link to="/about" className="nav-link">درباره ما </router-link></li>
        </ul>
    </div>
</div>
</nav>
</template>



<style>

</style>