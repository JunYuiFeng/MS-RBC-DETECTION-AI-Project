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
          <DropFile :multiple="true" @fileSelected="handlePatient1SelectedFiles" inputName="input1"/>
          <DropFile :multiple="true" @fileSelected="handlePatient2SelectedFiles" inputName="input2"/>
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
import DropFile from "/src/components/DropFile.vue";
import RBCComapredResults from "/src/components/RBCComparedResults.vue";
import { ref } from "vue";

const showRBCResults = ref(false);
const patient1 = ref<FileList | null>(null)
const patient2 = ref<FileList | null>(null)

const handlePatient1SelectedFiles = (files: FileList | null) => {
  if (files && files.length > 0) {
   patient1.value = files;
  }
};
const handlePatient2SelectedFiles = (files: FileList | null) => {
  if (files && files.length > 0) {
   patient2.value = files;
  }
};

const detect = () => {
  showRBCResults.value = true;
};
</script>

<style scoped></style>
