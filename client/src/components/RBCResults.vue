<template>
  <div class="bg-white p-10 w-1/2 rounded-3xl">
    <div class="text-2xl flex justify-start"><b>Model Result</b></div>
    <div class="grid grid-cols-12 gap-5">
      <div class="col-span-5">
        <div>image</div>
      </div>
      <div class="col-span-7">
        <div class="flex justify-start">Total Cells Detected</div>
        <div class="flex justify-start">372</div>

        <div class="flex justify-start">Healthy</div>
        <div class="flex justify-start">240</div>

        <div class="flex justify-start">Deformed Cells</div>
        <div class="flex justify-start">132</div>

        <div class="flex justify-start">Healthy Cells Percentage</div>
        <div class="flex justify-start">77%</div>

        <div class="flex justify-start">Deformed Cells Percentage</div>
        <div class="flex justify-start">23%</div>
      </div>
    </div>

    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">

    <div class="row">
      <div class="grid grid-cols-12 gap-10">
        <div class="col-span-6">
          <canvas id="chartPie"></canvas>
        </div>

        <div class="col-span-6" style="height: 200px;">
          <canvas id="chartBar"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';

// Register Chart.js and the plugin
Chart.register(...registerables, ChartDataLabels);

// Function to create a chart
const createChart = (elementId: string, type: string, data: any, options: any) => {
  const ctx = document.getElementById(elementId) as HTMLCanvasElement;
  new Chart(ctx, {
    type,
    data,
    options,
  });
};

// Data and configuration for the pie chart
const dataPie = {
  labels: ["Deformed", "Healthy"],
  datasets: [
    {
      data: [300, 50],
      backgroundColor: [
        "rgb(0,128,0)",
        "rgb(164, 101, 241)",
      ],
      hoverOffset: 4,
    },
  ],
};

const configPie = {
  plugins: {
    datalabels: {
      formatter: (value, context) => {
        let sum = 0;
        const dataArr = context.chart.data.datasets[0].data;
        dataArr.forEach((data) => {
          sum += data;
        });
        const percentage = ((value * 100) / sum).toFixed(2) + '%';
        return percentage;
      },
      color: '#fff',
    },
  },
};

// Data and configuration for the bar chart
const dataBar = {
  labels: ["Deformed", "Healthy"],
  datasets: [
    {
      data: [300, 50],
      backgroundColor: [
        "rgb(0,128,0)",
        "rgb(164, 101, 241)",
      ],
      hoverOffset: 4,
    },
  ],
};

const configBar = {
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};

onMounted(() => {
  // Create the charts
  createChart('chartPie', 'pie', dataPie, configPie);
  createChart('chartBar', 'bar', dataBar, configBar);
});
</script>


<style scoped></style>