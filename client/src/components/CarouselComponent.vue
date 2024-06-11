<template>
    <div class="relative w-full" data-carousel="static">
      <!-- Carousel wrapper -->
      <div class="relative h-56 overflow-hidden rounded-lg md:h-96">
        <!-- Carousel items -->
        <div
          v-for="(image, index) in images"
          :key="index"
          class="absolute inset-0 transition-opacity duration-700"
          :class="{'opacity-0': index !== currentIndex, 'opacity-100': index === currentIndex}"
        >
          <img
            :src="`data:image/jpg;base64,${image}`"
            class="block w-full h-full object-cover"
            alt="carousel item"
          />
        </div>
      </div>
      <!-- Slider indicators -->
      <div class="absolute z-30 flex -translate-x-1/2 space-x-3 bottom-5 left-1/2">
        <button
          v-for="(image, index) in images"
          :key="index"
          type="button"
          class="w-3 h-3 rounded-full"
          :class="{'bg-white': index === currentIndex, 'bg-gray-400': index !== currentIndex}"
          aria-current="index === currentIndex"
          @click="currentIndex = index"
          :aria-label="`Slide ${index + 1}`"
        ></button>
      </div>
      <!-- Slider controls -->
      <button
        type="button"
        class="absolute top-0 left-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
        @click="prevImage"
      >
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white">
          <svg class="w-4 h-4 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
          </svg>
          <span class="sr-only">Previous</span>
        </span>
      </button>
      <button
        type="button"
        class="absolute top-0 right-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none"
        @click="nextImage"
      >
        <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white">
          <svg class="w-4 h-4 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
          </svg>
          <span class="sr-only">Next</span>
        </span>
      </button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineProps } from 'vue';
  
  const props = defineProps<{
    images: string[];
  }>();
  
  const currentIndex = ref(0);
  
  const prevImage = () => {
    currentIndex.value = (currentIndex.value - 1 + props.images.length) % props.images.length;
  };
  
  const nextImage = () => {
    currentIndex.value = (currentIndex.value + 1) % props.images.length;
  };
  </script>
  
  <style scoped>
  .carousel-item {
    display: none;
  }
  
  .carousel-item-active {
    display: block;
  }
  </style>
  