<script setup>
import Vaziyat from "./Vaziyat.vue";
import UserAvatar from "./UserAvatar.vue";
import MenuSelect from "./MenuSelect.vue";

</script>
<template>
    <div class="container">
        <div class="row">
            <div class="col-12 col-lg-3">
                <div class="card bg-info my-5 p-5">
                    <img src="images/user.png" class="img-fluid rounded-circle d-block mx-auto" width="120px" height="120px" alt="user-image" >
                    <h5 class="text-white text-center mt-3">کاربر : علی نوروزی</h5>
                </div>
                <UserAvatar/>
            </div>

            <div class="col-12 col-lg-9">

                <div class="tab-content">
                <Vaziyat/>
                <MenuSelect/>
                </div>

            </div>

        </div>
    </div>
</template>


<style>

</style>