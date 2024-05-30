<template>
    <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
        <NavBar />
    </div>
    
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
        <RBCResults v-if="showRBCResults"/>
        
        <div v-else  class="bg-white p-10 w-1/2 rounded-3xl">
            <div class="text-2xl font-black flex justify-start mb-5">
                Upload an image to detect
            </div>
            <div>
                <div class="flex items-center gap-5 justify-center w-full">
                    <DropFile :multiple="false" />
                </div>
            </div>
            <div class="flex justify-center pt-10">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl" @click="detect">Detect RBC
                </button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import NavBar from '/src/components/NavBar.vue'
import DropFile from '/src/components/DropFile.vue'
import RBCResults from '/src/components/RBCResults.vue'
import { ref } from 'vue';

const showRBCResults = ref(false)

const detect= () => {
    showRBCResults.value = true
}

</script>

<style scoped>
</style>