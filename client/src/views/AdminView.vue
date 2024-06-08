<template>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
        <div class="bg-white p-10 w-1/2 rounded-3xl">
            
            <h1 class="text-2xl font-black pb-5">Admin Page</h1>
            <div class="flex justify-end">
                <button @click="openCreateModal" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl">
                    Add New User
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
                        <td class="p-3">{{ item.passwd }}</td>
                        <td class="flex justify-end gap-5 pt-3 pb-3">
                            <button @click="openEditModal(index)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl">
                                Edit User
                            </button>
                            <button @click="deleteUser(index)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-red-600 text-sm rounded-xl">
                                Delete User
                            </button>
                        </td>
                    </tr>                                
                </tbody>
            </table>  
            <div v-if="errorMessage" id="errorLabel" class="border border-red-400 rounded bg-red-100 px-4 py-3 mt-5 text-red-700 fade">{{ errorMessage }}</div>    
            <div v-if="successMessage" id="messageLabel" class="border border-green-400 rounded bg-green-100 px-4 py-3 mt-5 text-green-700 fade">{{ successMessage }}</div>   
            <UserModal v-if="showCreateModal" :user="selectedUser" :editMode="false" @close="closeModal"/>
            <UserModal v-if="showEditModal" :user="selectedUser" :editMode="true" @close="closeModal"/>
        </div>
    </div>
</template>


<script setup lang="ts">
import UserModal from '@/components/UserModal.vue';
import { onMounted, ref } from 'vue';

interface User {
    id: number;
    email: string;
    username: string;
    passwd: string;
}

const items = ref<User[]>([]);
const showCreateModal = ref(false);
const showEditModal = ref(false);
const headers = ['Email', 'Username', 'Password']
const selectedUser = ref<User | null>(null);
const errorMessage = ref<string | null>(null);
const successMessage = ref<string | null>(null);

const fetchUsers = async () => {
    try {
        const response = await fetch('http://localhost:5000/users');
        const data = await response.json();
        items.value = data.users;
    } catch (error) {
        showErrorLabel('Error fetching users');
    }
}

const deleteUser = async (index: number) => {
    const userToDelete = items.value[index];
    try {
        const response = await fetch(`http://localhost:5000/user/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: userToDelete.id })
        });
        if (response.ok) {
            items.value.splice(index, 1);
            showMessageLabel('User deleted successfully');
        } else {
            showErrorLabel('Failed to delete user');
        }
    } catch (error) {
        showErrorLabel('Error deleting user');
    }
}

const openCreateModal = () => {
    selectedUser.value = null;
    showCreateModal.value = true;
}

const openEditModal = (index: number) => {
    selectedUser.value = items.value[index];
    showEditModal.value = true;
}

const closeModal = () => {
    fetchUsers();
    showCreateModal.value = false;
    showEditModal.value = false;
}

const showMessageLabel = (message: string) => {
    successMessage.value = message;
    errorMessage.value = null;
    setTimeout(() => {
        successMessage.value = null;
    }, 3000);
}

const showErrorLabel = (message: string) => {
    errorMessage.value = message;
    successMessage.value = null;
    setTimeout(() => {
        errorMessage.value = null;
    }, 3000);
}

onMounted(() => {
    fetchUsers();
});

</script>

<style scoped> 
tr {
    border-bottom: 1px solid #ddd;
}

.edit-button {
    width: 100px; /* Adjust the width as needed */
}

.fade {
    transition: opacity 0.5s;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 1s;
}

.fade-enter,
.fade-leave-to /* .fade-leave-active in <2.1.8 */ {
    opacity: 0;
}

</style>