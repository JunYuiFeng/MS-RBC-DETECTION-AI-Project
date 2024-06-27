<template>
  <div class="grid grid-cols-12 gap-5">
    <!-- Conditional rendering of carousel or single image -->
    <div class="col-span-5">
        <CarouselComponent v-if="props.predictions.annotatedImages" :images="props.predictions.annotatedImages" />
        <img v-else :src="`data:image/jpg;base64,${props.predictions.annotatedImage}`" alt="blood smear example" class="rounded-lg w-full" />
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
          {{ props.predictions.totalCellsDetected }}
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
          {{ HealthyCellsPercentage }}%
        </div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells Percentage</b></div>
        <div class="flex justify-start font-black text-violet-700">
          {{ DeformedCellsPercentage }}%
        </div>
      </div>
      <h1 class="flex justify-start">{{ closestNumber(DeformedCellsPercentage) }}</h1>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";
import CarouselComponent from './CarouselComponent.vue'; // Ensure you have this component imported

const HealthyAVGDeformedPercentage = 15.8; // Derived from analysis of the dataset
const MSAVGDeformedPercentage = 24.6; // Derived from analysis of the dataset

const props = defineProps<{
  predictions: any;
  comparedResultsPage: boolean;
}>();

const HealthyCellsPercentage = Math.round((props.predictions.healthyCellsDetected * 100) / props.predictions.totalCellsDetected);

const DeformedCellsPercentage = Math.round((props.predictions.deformedCellsDetected * 100) / props.predictions.totalCellsDetected);

const closestNumber = (target: number): string => {
    const diff1 = Math.abs(target - HealthyAVGDeformedPercentage);
    const diff2 = Math.abs(target - MSAVGDeformedPercentage);

    if (diff1 > diff2) {
        return "*Potentially MS*";
    }
    return "";
};

</script>

<style scoped>
h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: orange;
}
</style>
