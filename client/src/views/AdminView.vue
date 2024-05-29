<template>
    <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
        <NavBar />
    </div>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
        <div class="bg-white p-10 w-1/2 rounded-3xl">
            
            <h1 class="text-2xl font-black pb-5">Admin Page</h1>
            <div class="flex justify-end">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl">
                    Add User
                </button>
            </div>
            <table class="w-full">
                <thead>
                    <tr>
                        <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in items" :key="index">
                        <td class="p-3">{{ item.email }}</td>
                        <td class="p-3">{{ item.username }}</td>
                        <td class="p-3">{{ item.password }}</td>
                            
                        <div class="flex justify-end gap-5 pt-3 pb-3">
                            <button
                                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl">Edit User
                            </button>
                            <button
                                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-red-600 text-sm rounded-xl">Delete User
                            </button>
                        </div>
                    </tr>
                </tbody>
        
            </table>  
        </div>
    </div>
</template>

<script setup lang="ts">
import NavBar from '/src/components/NavBar.vue'

const headers = ['Email', 'Username', 'Password']
const items = [
    { email: 'gmail.com', username: 'Jason', password: 'secret123' },
    { email: 'yahoo.com', username: 'Jun', password: 'secret123' },
    { email: 'hotmail.com', username: 'Sahib', password: 'secret123' },
    { email: 'outlook.com', username: 'Yvan', password: 'secret123' },
];


</script>

<style scoped> 
tr {
    border-bottom: 1px solid #ddd;
}
</style>