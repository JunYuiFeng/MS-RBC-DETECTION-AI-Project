<template>
    <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
        <NavBar />
    </div>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">

    <!-- <RBCInput/> -->
    <RBCResults/>

    </div>
</template>

<script setup lang="ts">
import NavBar from '/src/components/NavBar.vue'
import RBCInput from '/src/components/RBCInput.vue'
import RBCResults from '/src/components/RBCResults.vue'

</script>

<style scoped></style>