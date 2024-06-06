<template>
  <div class="grid grid-cols-12 gap-5">
    <div class="col-span-5">
      <img
        :src="`data:image/jpg;base64,${props.predictions.annotatedImage}`"
        alt="blood smear example"
        class="rounded-lg w-full"
      />
    </div>
    <div
      class="col-span-7 grid"
      :class="{
        'text-2xl gap-y-5': !props.comparedResultsPage,
      }"
    >
      <div>
        <div class="flex justify-start"><b>Total Cells Detected</b></div>
        <div class="flex justify-start font-black">{{props.predictions.healthyCellsDetected + props.predictions.deformedCellsDetected}}</div>
      </div>

      <div>
        <div class="flex justify-start"><b>Healthy</b></div>
        <div class="flex justify-start font-black text-green-600">{{props.predictions.healthyCellsDetected}}</div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells</b></div>
        <div class="flex justify-start font-black text-violet-700">{{props.predictions.deformedCellsDetected}}</div>
      </div>

      <div>
        <div class="flex justify-start"><b>Healthy Cells Percentage</b></div>
        <div class="flex justify-start font-black text-green-600">N/A</div>
      </div>

      <div>
        <div class="flex justify-start"><b>Deformed Cells Percentage</b></div>
        <div class="flex justify-start font-black text-violet-700">N/A</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps<{
  predictions: any;
  comparedResultsPage: boolean;
}>();
</script>

<style scoped></style>
