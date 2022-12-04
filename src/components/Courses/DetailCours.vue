<template>
    <div className="col-md-8">
                <div className="card mb-3">
                    <div className="card-header bg-white px-0 course-table">
                        <ul className="nav nav-justified pr-0">
                            <li className="nav-item"><a href="#course-info" className="nav-link active font-14" data-toggle="list">معرفی دوره</a></li>
                            <li className="nav-item"><a href="#comment" className="nav-link font-14" data-toggle="list">پرسش و پاسخ دوره</a></li>
                            <li className="nav-item"><a href="#teacher-info" className="nav-link font-14" data-toggle="list">درباره مدرس</a></li>
                        </ul>
                    </div>
                    <div className="card-body">
                        <div className="tab-content">
                            <div className="tab-pane active" id="course-info"><!-- Start course info -->

                                <h1 className="mb-3 text-info">آموزش HTML</h1>

                                <video src="" controls className="embed-responsive embed-responsive-item"></video>

                                <p className="text-justify course-text vazir font-14 my-5">
                                    برای اینکه وارد دنیای طراحی وب شوید اولین چیزی که باید با آن آشنا شوید HTML
                                    است، HTML یک زبانه نشانگذاری برای ایجاد وبسایت ها است
                                    که به ما این اجازه را میدهد، اسکلت وبسایت خود را به وجود آوریم .
                                    در این دوره من قصد دارم بدونه نیاز به هیچ پیش شرط به شما HTML 
                                    را آموزش دهم تا به شما کمک کنم اولین قدم برای ایجاد یک وبسایت را بر دارید . 
                                </p>

                                <h6 className="mb-3 mt-3">سر فصل ها :</h6>

                                <div className="mb-2 course-items px-2 py-4 d-flex align-items-center">
                                    <span className="bg-info count text-center text-white mr-3 font-13">1</span>
                                    <span className="mr-3 font-13">ساختار اصلی html - ابزار های مورد نیاز برای یادگیری - معرفی نرم افزار</span>
                                </div>

                                <div className="mb-2 course-items px-2 py-4 d-flex align-items-center">
                                    <span className="bg-info count text-center text-white mr-3 font-13">2</span>
                                    <span className="mr-3 font-13">آشنایی با تگ ها ، معرفی برخی از تگ ها ، دسته بندی تگ ها ، ساختار تگ های Index </span>
                                </div>

                                <div className="mb-2 course-items px-2 py-4 d-flex align-items-center">
                                    <span className="bg-info count text-center text-white mr-3 font-13">3</span>
                                    <span className="mr-3 font-13">نرم ا فزار استفاده شده در اموزش ، ایجاد سند ، tag a و tag p و تشریح کد های html - t head body </span>
                                </div>

                                <div className="mb-2 course-items px-2 py-4 d-flex align-items-center">
                                    <span className="bg-info count text-center text-white mr-3 font-13">4</span>
                                    <span className="mr-3 font-13">آشنایی کامل با اَتریبیوت ها در Html 5 </span>
                                </div>

                                <div className="mb-2 course-items px-2 py-4 d-flex align-items-center product-link">
                                    <span className="bg-info count text-center text-white mr-3 font-13">5</span>
                                    <span className="mr-3 font-13">کار با متون در html 5 ، تگ p ، تگ h ، تگ span ، تگ hr و بررسی تفاوت ها و کاربرد های مخصوص هر تگ </span>
                                </div>
                            </div><!-- End course info -->

                            <div className="tab-pane fade" id="comment"><!-- Start comment -->

                                <form action="" method="">
                                    <div className="row">
                                        <div className="col form-group">
                                            <input type="text" id="name" className="form-control rounded-pill" placeholder="نام خود را وارد کنید ...">
                                        </div>
                                        <div className="col form-group">
                                            <input type="email" id="email" className="form-control rounded-pill" placeholder="ایمیل خود را وارد کنید ...">
                                        </div>
                                    </div>
                                    <div className="form-group">
                                        <textarea  cols="30" rows="10" className="form-control w-100 rounded-lg p-3" placeholder="دیدگاه خود را وارد کنید ..."></textarea>
                                    </div>
                                    <section className='rating-widget mt-2'><!-- star rating-->
                                        <div className='rating-stars'>
                                            <ul id='stars'>
                                                <li className='star' data-tooltip='ضعیف' data-value='1'>
                                                    <i className='fa fa-star fa-fw'></i>
                                                </li>
                                                <li className='star' data-tooltip='متوسط' data-value='2'>
                                                    <i className='fa fa-star fa-fw'></i>
                                                </li>
                                                <li className='star' data-tooltip='خوب' data-value='3'>
                                                    <i className='fa fa-star fa-fw'></i>
                                                </li>
                                                <li className='star' data-tooltip='خیلی خوب' data-value='4'>
                                                    <i className='fa fa-star fa-fw'></i>
                                                </li>
                                                <li className='star' data-tooltip='عالی' data-value='5'>
                                                    <i className='fa fa-star fa-fw'></i>
                                                </li>
                                            </ul>
                                        </div>
                                    </section>
                                    <button type="submit" className="btn btn-primary rounded-pill mr-auto d-block font-13">ارسال</button>
                                </form>

                                <div className="bg-light my-3 p-2 pb-4">
                                    <div className="d-flex align-items-center">
                                        <p className="text-danger mb-0 vazir font-13">arash</p>
                                        <small className="mx-5 text-muted">15 تیر 1398</small>
                                    </div>
                                    <p className="text-justify my-2 vazir font-13">آیا آموزش های این دوره تموم شده یا هنوز ادامه داره ؟! </p>

                                    <div className=" shadow-sm mr-5 w-75 mt-3 p-2 bg-white">
                                        <div className="d-flex align-items-center">
                                            <p className="text-danger mb-0 vazir font-13">Admin</p>
                                            <small className="mx-5 text-muted">15 تیر 1398</small>
                                        </div>
                                        <p className="text-justify my-2 vazir font-13">سلام بزودی قسمت های جدید آپلود خواهد شد.</p>
                                    </div>

                                </div>


                            </div><!-- End comment -->

                            <div className="tab-pane fade" id="teacher-info"><!-- Start teacher info -->

                                <img src="images/teacher.jpg" alt="" className="img-fluid d-block mx-auto">

                                <p className="text-justify mt-5 vazir font-14">اول داستان، طراح گرافیک بودم و ۲ سالی به عنوان طراح مشغول بودم،
                                    بعد به برنامه‌نویسی علاقمند شدم و الان بیشتر
                                    از ۱۰ ساله که عاشق کدزنی و چالش‌های پروژه‌های مختلفم. به تدریس علاقه خاصی دارم 
                                    و دوست دارم دانشی که در این راه بدست آوردم را در اختیار دیگران هم قرار بدم.
                            </p>

                                <table className="table table-striped table-bordered text-center my-5  font-14">
                                    <tr>
                                        <td>نام مدرس</td>
                                        <td>مقطع تحصیلی</td>
                                        <td>رشته</td>
                                        <td>دانشگاه</td>
                                    </tr>
                                    <tr>
                                        <td>علی نوروزی</td>
                                        <td>لیسانس</td>
                                        <td>گرافیک</td>
                                        <td>آزاد</td>
                                    </tr>
                                </table>

                                <h6 className="mb-4">مهارت ها :</h6>

                                <div className="progress mb-4">
                                    <div className="progress-bar bg-success" style="width: 95%;">Html (95%)</div>
                                </div>
                                <div className="progress mb-4">
                                    <div className="progress-bar bg-success" style="width: 98%;">Css (98%)</div>
                                </div>
                                <div className="progress mb-4">
                                    <div className="progress-bar bg-success" style="width: 80%;">Javascript (80%)</div>
                                </div>
                                <div className="progress mb-4">
                                    <div className="progress-bar bg-success" style="width: 70%;">Jquery (70%)</div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>

</template>

<script setup>

</script>

<style>

</style>