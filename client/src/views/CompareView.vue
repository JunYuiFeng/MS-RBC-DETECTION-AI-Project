<template>
  <div
    class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600"
  >
    <RBCComapredResults v-if="showRBCResults" />

    <div v-else class="bg-white p-10 w-1/2 rounded-3xl">
      <div class="text-2xl font-black flex justify-start mb-5">
        Upload one or more images to compare
      </div>
      <div>
        <div class="flex items-center gap-5 justify-center w-full">
          <DropFile :multiple="true" />
          <DropFile :multiple="true" />
        </div>
      </div>
      <div class="flex justify-center pt-10">
        <button
          class="hover:bg-blue-700 text-white font-bold py-2 px-4 bg-indigo-950 text-sm rounded-xl"
          @click="detect"
        >
          Detect RBC
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import NavBar from "/src/components/NavBar.vue";
import DropFile from "/src/components/DropFile.vue";
import RBCComapredResults from "/src/components/RBCComparedResults.vue";
import { ref } from "vue";

const showRBCResults = ref(false);

const detect = () => {
  showRBCResults.value = true;
};
</script>

<style scoped></style>
