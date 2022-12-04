<script setup>

import DetailCours from './DetailCours.vue';
import InfoCours from './InfoCours.vue';
import SatusMenu from './SatusMenu.vue';


</script>
<template>
    <SatusMenu/>
    <div className="container">
        <div className="row">
            <InfoCours/>
            <DetailCours/>
        </div>
    </div>
</template>



<style>

</style>