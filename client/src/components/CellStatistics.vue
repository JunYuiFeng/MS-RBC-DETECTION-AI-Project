<template>
  <div class="grid grid-cols-12 gap-5">
    <!-- Conditional rendering of carousel or single image -->
    <div class="col-span-5">
      <div v-if="props.comparedResultsPage">
        <CarouselComponent v-if="props.predictions.annotatedImages" :images="props.predictions.annotatedImages" />
        <img v-else :src="`data:image/jpg;base64,${props.predictions.annotatedImage}`" alt="blood smear example" class="rounded-lg w-full" />
      </div>
      <div v-else>
        <img :src="`data:image/jpg;base64,${props.predictions.annotatedImage}`" alt="blood smear example" class="rounded-lg w-full" />
      </div>
    </div>

    <div
      class="col-span-7 grid"
      :class="{
        'text-2xl gap-y-5': !props.comparedResultsPage,
      }"
    >
      <div>
        <div class="flex justify-start"><b>Total Cells Detected</b></div>
        <div class="flex justify-start font-black">
          {{ props.predictions.healthyCellsDetected + props.predictions.deformedCellsDetected }}
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Healthy</b></div>
        <div class="flex justify-start font-black text-green-600">
          {{ props.predictions.healthyCellsDetected }}
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells</b></div>
        <div class="flex justify-start font-black text-violet-700">
          {{ props.predictions.deformedCellsDetected }}
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Healthy Cells Percentage</b></div>
        <div class="flex justify-start font-black text-green-600">
          {{ Math.round((props.predictions.healthyCellsDetected * 100) / (props.predictions.deformedCellsDetected + props.predictions.healthyCellsDetected)) }}%
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells Percentage</b></div>
        <div class="flex justify-start font-black text-violet-700">
          {{ Math.round((props.predictions.deformedCellsDetected * 100) / (props.predictions.deformedCellsDetected + props.predictions.healthyCellsDetected)) }}%
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import CarouselComponent from './CarouselComponent.vue'; // Ensure you have this component imported

const props = defineProps<{
  predictions: any;
  comparedResultsPage: boolean;
}>();
</script>

<style scoped></style>
