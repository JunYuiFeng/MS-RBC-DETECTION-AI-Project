<template>
  <div class="grid grid-cols-12 gap-5">
    <!-- Use the carousel component -->
    <div class="col-span-5">
      <CarouselComponent :images="props.predictions.annotatedImages || [props.predictions.annotatedImage]" />
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
          {{ ((props.predictions.healthyCellsDetected * 100) / (props.predictions.deformedCellsDetected + props.predictions.healthyCellsDetected)).toFixed(2) + "%" }}
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells Percentage</b></div>
        <div class="flex justify-start font-black text-violet-700">
          {{ ((props.predictions.deformedCellsDetected * 100) / (props.predictions.deformedCellsDetected + props.predictions.healthyCellsDetected)).toFixed(2) + "%" }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import CarouselComponent from './CarouselComponent.vue';

const props = defineProps<{
  predictions: any;
  comparedResultsPage: boolean;
}>();
</script>

<style scoped></style>
