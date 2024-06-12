<template>
    <div class="bg-white p-10 w-3/4 rounded-3xl">
        <div class="text-2xl flex justify-start font-black">Model Result</div>
        <div class="grid grid-cols-2 gap-4">
            <div>
                <div class="flex justify-start font-black"><b>Sample <span style="color: rgb(156,68,68);">A</span></b>
                </div>
                <CellStatistics :comparedResultsPage="true" :predictions="comparisons.patient1" />
            </div>
            <div>
                <div class="flex justify-start font-black"><b>Sample <span style="color: rgb(56,60,148);">B</span></b>
                </div>
                <CellStatistics :comparedResultsPage="true" :predictions="comparisons.patient2" />
            </div>
        </div>

        <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">

        <div class="row">
            <div class="grid grid-cols-12 gap-10">
                <div class="col-span-4">
                    <canvas id="chartPie" class="p-10"></canvas>
                </div>

                <div class="col-span-4 ">
                    <canvas id="chartBar" class="mt-12"></canvas>
                </div>

                <div class="col-span-4 pt-10 ">
                    <div class="text-lg font-bold flex justify-start mb-4">Insights</div>
                    <ul>
                        <li class="flex justify-start text-xs mb-4 font-bold"> &#8226; Sample B contains {{ deformedCellsPercentageDifference
                            }}% more deformed cells</li>
                        <li class="flex justify-start text-xs font-bold">&#8226; Sample B contains {{ healthyCellsPercentageDifference }}%
                            less healthy cells</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, defineProps, ref } from 'vue';
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import CellStatistics from '/src/components/CellStatistics.vue';
import { ComparisonResponse } from '@/services/api';

const props = defineProps<{
    comparisons: ComparisonResponse;
}>();

// Register Chart.js and the plugin
Chart.register(...registerables, ChartDataLabels);

const deformedCellsPercentageDifference = ref(0);
const healthyCellsPercentageDifference = ref(0);

// Function to calculate the percentage differences
const calculatePercentageDifferences = () => {
    const { patient1, patient2 } = props.comparisons;

    const totalCellsA = patient1.deformedCellsDetected + patient1.healthyCellsDetected;
    const totalCellsB = patient2.deformedCellsDetected + patient2.healthyCellsDetected;

    deformedCellsPercentageDifference.value = Math.abs(Math.round(((patient1.deformedCellsDetected - patient2.deformedCellsDetected) / totalCellsA) * 100));
    healthyCellsPercentageDifference.value = Math.abs(Math.round(((patient1.healthyCellsDetected - patient2.healthyCellsDetected) / totalCellsB) * 100));
};

// Function to create a chart
const createChart = (elementId: string, type: string, data: any, options: any) => {
    const ctx = document.getElementById(elementId) as HTMLCanvasElement;
    new Chart(ctx, {
        type,
        data,
        options,
    });
};

// Function to update charts
const updateCharts = () => {
    calculatePercentageDifferences();

    // Data for the pie chart
    const dataPie = {
        labels: ["Sample A Deformed cells", "Sample B Deformed cells"],
        datasets: [
            {
                data: [
                    props.comparisons.patient1.deformedCellsDetected,
                    props.comparisons.patient2.deformedCellsDetected,
                ],
                backgroundColor: ["rgb(156,68,68)", "rgb(56,60,148)"],
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

    // Data for the bar chart
    const dataBar = {
        labels: ["Deformed", "Healthy"],
        datasets: [
            {
                label: 'Sample A',
                data: [
                    props.comparisons.patient1.deformedCellsDetected,
                    props.comparisons.patient1.healthyCellsDetected,
                ],
                backgroundColor: "rgb(156,68,68)",
                hoverOffset: 4,
            },
            {
                label: 'Sample B',
                data: [
                    props.comparisons.patient2.deformedCellsDetected,
                    props.comparisons.patient2.healthyCellsDetected,
                ],
                backgroundColor: "rgb(56,60,148)",
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
        plugins: {
            datalabels: {
                color: '#fff',
            },
        },
    };

    createChart('chartPie', 'pie', dataPie, configPie);
    createChart('chartBar', 'bar', dataBar, configBar);
};

onMounted(() => {
    updateCharts();
});

//   watch(() => props.comparisons, updateCharts, { deep: true });
</script>

<style scoped></style>