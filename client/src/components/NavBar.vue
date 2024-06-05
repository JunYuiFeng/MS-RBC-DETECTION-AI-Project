<script setup lang="ts">
import { ref, watch } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const toggledButton = ref<string | null>(null);

watch(
  () => router.currentRoute.value.name,
  (newName) => {
    if (newName) toggledButton.value = newName.toString();
  },
  { immediate: true }
);

const toggleButton = (button: string) => {
  if (button === "Comparison") {
    router.push({ name: "Comparison" });
  } else if (button === "RBCDetection") {
    router.push({ name: "RBCDetection" });
  }
};
</script>

<template>
  <nav class="flex bg-transparent font-bold justify-between p-3">
    <router-link :to="{ name: 'RBCDetection' }" class="text-xl text-white">
      Healthy and Deformed Cells AI Detection
    </router-link>
    <div class="text-white flex space-x-2">
      <button
        :class="[
          'rounded rounded-2xl p-2',
          toggledButton === 'RBCDetection'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('RBCDetection')"
      >
        RBC Detection
      </button>
      <button
        :class="[
          'rounded rounded-2xl p-2',
          toggledButton === 'Comparison'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('Comparison')"
      >
        RBC Image Comparison
      </button>
    </div>
  </nav>
</template>

<style scoped></style>
