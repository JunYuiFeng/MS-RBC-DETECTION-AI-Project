<template>
    <div class="flex justify-center mt-10 min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">
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
                    <tr v-for="(user, index) in users" :key="index">
                        <td class="p-3">{{ user.email }}</td>
                        <td class="p-3">{{ user.username }}</td>
                        <td class="p-3">●●●●●●●</td>
                        <td class="flex justify-end gap-5 pt-3 pb-3">
                            <button @click="openEditModal(user)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 text-sm rounded-xl">
                                Edit User
                            </button>
                            <button v-if="user.role != 'ADMIN'" @click="handleDeleteUser(user.id)" class="hover:bg-blue-700 text-white font-bold py-2 px-4 bg-red-600 text-sm rounded-xl">
                                Delete User
                            </button>
                        </td>
                    </tr>                                
                </tbody>
            </table>  
            <div v-if="errorMessage" id="errorLabel" class="border border-red-400 rounded bg-red-100 px-4 py-3 mt-5 text-red-700 fade">{{ errorMessage }}</div>    
            <div v-if="successMessage" id="messageLabel" class="border border-green-400 rounded bg-green-100 px-4 py-3 mt-5 text-green-700 fade">{{ successMessage }}</div>   
            <UserModal v-if="showCreateModal" :user="selectedUser" :editMode="false" @close="closeModal" @confirm="handleConfirm"/>
            <UserModal v-if="showEditModal" :user="selectedUser" :editMode="true" @close="closeModal" @confirm="handleConfirm"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import UserModal from '@/components/UserModal.vue';
import { onMounted, ref } from 'vue';
import { useFetchUsers } from '@/composables/useFetchUsers';
import { useDeleteUser } from '@/composables/useDeleteUser';
import { User } from '@/services/api';

const showCreateModal = ref(false);
const showEditModal = ref(false);
const headers = ['Email', 'Username', 'Password']
const selectedUser = ref<User | null>(null);
const errorMessage = ref<string | null>(null);
const successMessage = ref<string | null>(null);

const { fetchUsers, users, fetchUserError } = useFetchUsers();
const { deleteUser, deleteUserError } = useDeleteUser();

// Handle delete user
const handleDeleteUser = async (id: number) => {
    await deleteUser(id);

    if (deleteUserError.value) {
        showErrorLabel('Error deleting user');
    } else {
        showMessageLabel('User deleted successfully');
        await fetchUsers();
    }
}

// Open create modal
const openCreateModal = () => {
    selectedUser.value = null;
    showCreateModal.value = true;
}

// Open edit modal
const openEditModal = (user: User) => {
    selectedUser.value = user;
    showEditModal.value = true;
}

// Close modal
const closeModal = () => {
    showCreateModal.value = false;
    showEditModal.value = false;
}

// Close model and show message label
const handleConfirm = async () => {
    await fetchUsers();

    if (fetchUserError.value) {
        showErrorLabel('Error fetching users');
    } else {
        if (showCreateModal.value) {
            showMessageLabel('User created successfully');
        } else if (showEditModal.value) {
            showMessageLabel('User updated successfully');
        }
    }

    closeModal();
}

// Show message label
const showMessageLabel = (message: string) => {
    successMessage.value = message;
    errorMessage.value = null;

    setTimeout(() => {
        successMessage.value = null;
    }, 2000);
}

// Show error label
const showErrorLabel = (message: string) => {
    errorMessage.value = message;
    successMessage.value = null;

    setTimeout(() => {
        errorMessage.value = null;
    }, 2000);
}

onMounted(async () => {
    await fetchUsers();

    if (fetchUserError.value) {
        showErrorLabel('Error fetching users');
    }    
});
</script>

<!-- Fade effects for labels -->
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
.fade-leave-to {
    opacity: 0;
}
</style>
