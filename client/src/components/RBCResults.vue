<template>
  <div class="bg-white p-10 w-1/2 rounded-3xl">
    <div class="text-2xl flex justify-start font-black mb-3">Model Result</div>
    <CellStatistics/>

    <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">

    <div class="row">
      <div class="grid grid-cols-12 gap-10">
        <div class="col-span-6">
          <canvas id="chartPie" class="p-10"></canvas>
        </div>

        <div class="col-span-6 ">
          <canvas id="chartBar" class="mt-12"></canvas>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import CellStatistics from '/src/components/CellStatistics.vue';

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
      label: 'Cell Count',
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
      max: 500,
    },
  },
  plugins: {
    datalabels: {
      color: '#fff', 
    },
  },
};

onMounted(() => {
  createChart('chartPie', 'pie', dataPie, configPie);
  createChart('chartBar', 'bar', dataBar, configBar);
});
</script>


<style scoped></style>