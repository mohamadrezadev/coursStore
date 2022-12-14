<template>
      <div className="container">
        <div className="row">
            <div className="col-sm-12 d-flex justify-content-between">
                <h6 className="title pb-2">
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