<template>
    <nav class="flex bg-transparent font-bold justify-between p-3">
        <div class="text-xl text-white">
            Healthy and Deformed Cells AI Detection
        </div>
        <div class="text-white flex space-x-2">
            <button 
                :class="{
                    'bg-white text-black': toggledButton === 'RBCDetection', 
                    'bg-gray-400 text-white': toggledButton !== 'RBCDetection'
                }" 
                class="rounded rounded-2xl p-2" 
                @click="toggleButton('RBCDetection')">
                RBC Detection
            </button>
            <button 
                :class="{
                    'bg-white text-black': toggledButton === 'RBCComparison', 
                    'bg-gray-400 text-white': toggledButton !== 'RBCComparison'
                }" 
                class="rounded rounded-2xl p-2" 
                @click="toggleButton('RBCComparison')">
                RBC Image Comparison
            </button>
        </div>
    </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const toggledButton = ref<string | null>(null);

const toggleButton = (button: string) => {
    if (toggledButton.value === button) {
        toggledButton.value = null; // Untoggle if the same button is clicked again
    } else {
        toggledButton.value = button; // Toggle the clicked button
    }
}
</script>

<style scoped>

</style>
