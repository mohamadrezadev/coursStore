<template>
      <div class="container">
        <div class="row">
            <div class="col-sm-12 d-flex justify-content-between">
                <h6 class="title pb-2">
                    {{title}}
                </h6>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps({
  title: String
})
</script>

<style>

</style>