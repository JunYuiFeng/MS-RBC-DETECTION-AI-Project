<template>
    <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
        <NavBar />
    </div>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
        <div class="bg-white p-10 w-1/2 rounded-3xl">
            <table>
                <thead>
                    <tr>
                        <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in items" :key="index">
                        <td>{{ item.email }}</td>
                        <td>{{ item.username }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import NavBar from '/src/components/NavBar.vue'

const headers = ['Email', 'Username', ]
const items = [
    { email: 'gmail.com', username: 'Jason' },
    { email: 'yahoo.com', username: 'Jun' },
    { email: 'hotmail.com', username: 'Sahib' },
    { email: 'outlook.com', username: 'Yvan' },
];


</script>

<style scoped></style>