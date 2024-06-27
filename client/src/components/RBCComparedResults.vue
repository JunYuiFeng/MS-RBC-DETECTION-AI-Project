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
                        <li class="flex justify-start text-xs mb-4 font-bold"> &#8226;{{ insight }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, defineProps, ref, toRefs } from 'vue';
import { Chart, ChartTypeRegistry, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import CellStatistics from '/src/components/CellStatistics.vue';
import { ComparisonResponse } from '@/services/api';

const props = defineProps<{
    comparisons: ComparisonResponse;
}>();

// Register Chart.js and the plugin
Chart.register(...registerables, ChartDataLabels);

const { comparisons } = toRefs(props);
const { patient1, patient2 } = comparisons.value;

const patient1HealthyCellsPercentage = Math.round((patient1.healthyCellsDetected * 100) / patient1.totalCellsDetected);
const patient1DeformedCellsPercentage = Math.round((patient1.deformedCellsDetected * 100) / patient1.totalCellsDetected);

const patient2HealthyCellsPercentage = Math.round((patient2.healthyCellsDetected * 100) / patient2.totalCellsDetected);
const patient2DeformedCellsPercentage = Math.round((patient2.deformedCellsDetected * 100) / patient2.totalCellsDetected);

const insight = ref('');

// Function to calculate the percentage differences
const generateInsight = () => {
    const result = Math.abs(patient1DeformedCellsPercentage - patient2DeformedCellsPercentage);

    if (patient1DeformedCellsPercentage > patient2DeformedCellsPercentage) {
        insight.value = `Sample B has ${result}% fewer deformed cells than Sample A`;
    } else {
        insight.value = `Sample B has ${result}% more deformed cells than Sample A`;
    }
};

// Function to create a chart
const createChart = (elementId: string, type: keyof ChartTypeRegistry, data: any, options: any) => {
    const ctx = document.getElementById(elementId) as HTMLCanvasElement;
    new Chart(ctx, {
        type,
        data,
        options,
    });
};

// Function to update charts
const updateCharts = () => {
    generateInsight();

    // Data for the pie chart
    const dataPie = {
        labels: ["Sample A Deformed cells", "Sample B Deformed cells"],
        datasets: [
            {
                data: [
                    patient1DeformedCellsPercentage,
                    patient2DeformedCellsPercentage,
                ],
                backgroundColor: ["rgb(156,68,68)", "rgb(56,60,148)"],
                hoverOffset: 4,
            },
        ],
    };

    const configPie = {
        plugins: {
            datalabels: {
                formatter: (value: any, context: any) => {
                    let sum = 0;
                    const dataArr = context.chart.data.datasets[0].data;
                    dataArr.forEach((data: any) => {
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
                    patient1DeformedCellsPercentage,
                    patient1HealthyCellsPercentage,
                ],
                backgroundColor: "rgb(156,68,68)",
                hoverOffset: 4,
            },
            {
                label: 'Sample B',
                data: [
                    patient2DeformedCellsPercentage,
                    patient2HealthyCellsPercentage,
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

</script>

<style scoped></style>