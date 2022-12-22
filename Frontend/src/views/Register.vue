<script setup>
import axios from 'axios';
import {onMounted, ref } from 'vue';
import {useRouter} from 'vue-router';
import { toast } from 'vue3-toastify';

const form ={
     "name" :'',
    "username" :'',
    "email" :'',
    "password":''
}
const notify = (text) => {
      toast.success(text, {
        autoClose: 2000,
      }); // ToastOptions
    }


const router =useRouter()
const OnSubmitForm=()=>{
     axios.post ("http://127.0.0.1:8000/signup",form)
     .then(response => {
        if (response.data) {
          notify("ثبت نام موفقیت امیز بود")
          localStorage.setItem('TOKEN',response.data.access_token)
          router.push({ path: '/' })
        }
        return response.data;
      });
}
</script>

<template>
  <div class="container">
    <div class="row d-flex justify-content-center">
      <div class="col-lg-7 col-xl-6 col-md-9 register">
        <div class="card my-5">
          <div class="card-body">
            <h5 class="shadow-sm text-center mb-4 py-3">عضویت در سایت</h5>

            <form @submit.prevent='OnSubmitForm'>
              <div class="form-group">
                <label for="name"> نام و نام خانوادگی: </label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text my-icon"
                      ><i class="fa fa-user align-middle"></i
                    ></span>
                  </div>
                  <input
                    v-model.lazy="form.name"
                    type="text"
                    class="form-control"
                    id="name"
                    placeholder="نام و نام خانوادگی خود را وارد کنید"
                  />
                </div>
              </div>

              <div class="form-group">
                <label for=""> ایمیل : </label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text my-icon">
                      <i class="fa fa-envelope align-middle"></i
                    ></span>
                  </div>
                  <input
                    v-model.lazy="form.email"
                    type="text"
                    class="form-control"
                    placeholder=" ایمیل خود را وارد کنید"
                  />
                </div>
              </div>

              <div class="form-group">
                <label for="">نام کاربری : </label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text my-icon">
                      <i class="fa fa-user-plus align-middle"></i
                    ></span>
                  </div>
                  <input
                    v-model.lazy="form.username"
                    type="text"
                    class="form-control"
                    placeholder="نام کاربری خود را وارد کنید "
                  />
                </div>
              </div>

              <div class="form-group">
                <label for=""> رمز عبور : </label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text my-icon">
                      <i class="fa fa-lock align-middle"></i
                    ></span>
                  </div>
                  <input
                    v-model.lazy="form.password"
                    type="password"
                    class="form-control"
                    placeholder="رمز عبور خود را وارد کنید"
                  />
                </div>
              </div>
              <button
                type="submit"
                class="btn btn-primary btn-block rounded-pill custom-btn font-13 mt-4"
              >
                ثبت نام
              </button>

              <p class="text-center my-3 font-12 vazir">
                قبلا در سایت ثبت نام کرده اید ؟
                <a href="" class="login vazir"
                  ><router-link to="/login"> وارد شوید </router-link>
                </a>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style></style>
