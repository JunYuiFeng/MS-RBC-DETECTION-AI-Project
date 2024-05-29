<template>
    <div class="bg-white p-10 w-1/2 rounded-3xl">
      <div class="grid grid-cols-12 gap-1">
        <div class="col-span-4">
          <div class="text-2xl"><b>Model Result</b></div>
        </div>
        <div class="col-span-8">
          <div>data</div>
        </div>
      </div>
  
      <div class="row">
          <div class="columns-2">
            <div class="shadow-lg rounded-lg overflow-hidden" style="width: fit-content;">
              <canvas class="p-1 ml-40 mr-40" id="chartPie"></canvas>
            </div>
      
            <div class="shadow-lg rounded-lg overflow-hidden" style="width: fit-content;">
              <canvas class="p-1 ml-40 mr-40" id="chartBar"></canvas>
            </div>
          </div>
        </div>
      </div>
  </template>
  
  <script setup lang="ts">
  import { onMounted } from 'vue';
  import { Chart, registerables } from 'chart.js';
  
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
    type: "pie",
    data: dataPie,
    options: {},
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
    type: "bar",
    data: dataBar,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  };
  
  onMounted(() => {
    // Register the necessary components for Chart.js
    Chart.register(...registerables);
  
    // Create the charts
    createChart('chartPie', 'pie', dataPie, {});
    createChart('chartBar', 'bar', dataBar, configBar.options);
  });
  </script>
  
  <style scoped></style>
  