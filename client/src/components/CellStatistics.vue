<template>
    <div class="grid grid-cols-12 gap-5">
      <div class="col-span-5">
        <img src="@/assets/blood-smear-example.jpg" alt="blood smear example" class="rounded-lg" style="width: 80%;">
      </div>
      <div class="col-span-7 grid" :class="{
      'text-2xl gap-y-5': !props.comparedResultsPage}">
        <div>
          <div class="flex justify-start"><b>Total Cells Detected</b></div>
          <div class="flex justify-start font-black">372</div>
        </div>
  
        <div>
          <div class="flex justify-start"><b>Healthy</b></div>
          <div class="flex justify-start font-black text-green-600">240</div>
        </div>
  
        <div>
          <div class="flex justify-start"><b>Deformed Cells</b></div>
          <div class="flex justify-start font-black text-violet-700">132</div>
        </div>
  
        <div>
          <div class="flex justify-start"><b>Healthy Cells Percentage</b></div>
          <div class="flex justify-start font-black text-green-600">77%</div>
        </div>
  
        <div>
          <div class="flex justify-start"><b>Deformed Cells Percentage</b></div>
          <div class="flex justify-start font-black text-violet-700">23%</div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { defineProps } from 'vue';

  const props = defineProps<{
    comparedResultsPage: boolean;
  }>();
  </script>
  
  <style scoped>
  </style>
  