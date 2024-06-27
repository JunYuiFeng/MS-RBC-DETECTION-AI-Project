<template>
  <div
  class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
    <RBCResults v-if="prediction" :predictions="prediction" />

    <div v-else class="bg-white p-10 w-1/2 rounded-3xl">
      <div class="text-2xl font-black flex justify-start mb-5">
        Upload an image to detect
      </div>
      <div>
        <div class="flex items-center gap-5 justify-center w-full">
          <DropFile :multiple="true" @fileSelected="handleSelectedFile" />
        </div>
      </div>
      <div v-if="error" class="text-red-500 mt-3">{{ error }}</div>
      <div class="flex justify-center mt-3">
        <LoadingSpinner v-if="isLoading" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import DropFile from "/src/components/DropFile.vue";
import RBCResults from "/src/components/RBCResults.vue";
import usePredict from "@/composables/usePredict";
import LoadingSpinner from "@/components/LoadingSpinner.vue";

const { prediction, isLoading, error, predictImages, hasPrediction } = usePredict();

// Put files into array and predict
const handleSelectedFile = (files: FileList | null) => {
  if (files && files.length > 0) {
    const imageFiles = Array.from(files); // Convert FileList to an array of files
    predictImages(imageFiles); // Pass the array to predictImages
  }
};
</script>


<style scoped></style>
