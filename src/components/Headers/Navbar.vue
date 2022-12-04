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
            <li className="nav-item ml-3 custom-nav-item"><a href="index.html" className="nav-link">صفحه اصلی</a></li>
            <li className="nav-item ml-3 dropdown custom-nav-item"><a href="#" className="nav-link  dropdown-toggle" data-toggle="dropdown">دوره های آموزشی</a>

                <div className="dropdown-menu custom-dropdown-menu dropdown-menu-right font-13 text-right">
                    <a href="course.html" className="dropdown-item border-bottom py-2">دوره متخصص طراحی سایت</a>
                    <a href="course.html" className="dropdown-item border-bottom py-2">دوره آموزش برنامه نویسی اندروید</a>
                    <a href="course.html" className="dropdown-item border-bottom py-2">دوره  جامع آموزش فتوشاپ</a>
                    <a href="course.html" className="dropdown-item border-bottom py-2">دوره آموزش پایتون</a>
                    <a href="course.html" className="dropdown-item py-2">دوره جامع آموزش وردپرس</a>
                </div>

            </li>
            <li className="nav-item ml-3 dropdown custom-nav-item"><a href="#" className="nav-link  dropdown-toggle" data-toggle="dropdown">صفحات</a>

                <div className="dropdown-menu  custom-dropdown-menu dropdown-menu-right font-13 text-right">
                    <a href="panel-user.html" className="dropdown-item border-bottom py-2">پنل کاربری</a>
                    <a href="search.html" className="dropdown-item border-bottom py-2">جستجو</a>
                    <a href="error404.html" className="dropdown-item py-2">Error 404</a>
                </div>

            </li>
            <li className="nav-item ml-3 custom-nav-item"><a href="blog.html" className="nav-link">بلاگ</a></li>
            <li className="nav-item ml-3 custom-nav-item"><a href="contact-us.html" className="nav-link">تماس باما</a></li>
        </ul>
    </div>
</div>
</nav>
</template>



<style>

</style>