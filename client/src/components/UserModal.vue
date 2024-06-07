<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-50">
        <div class="text-left bg-white p-5 rounded-xl w-1/3">
            <div>
                <div class="mb-4">
                    <label class="block text-gray-700">Email:</label>
                    <input v-model="email"  type="email" class="w-full px-3 py-2 border rounded"/>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Username:</label>
                    <input v-model="username" type="text" class="w-full px-3 py-2 border rounded"/>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Password:</label>
                    <input v-model="password" type="text" class="w-full px-3 py-2 border rounded"/>
                </div>
                <div class="flex justify-end gap-4">
                    <button @click="$emit('close')" type="button" class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded">Cancel</button>
                    <button @click="handleSubmit" class="bg-green-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Confirm</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps, ref, onMounted } from 'vue';

const props = defineProps({
    editMode: {
        type: Boolean,
        default: null,
    },
    user: {
        type: Object,
        default: null,
    },
});

const resetForm = () => {
    email.value = '';
    username.value = '';
    password.value = '';
};

const email = ref('email');
const username = ref('username');
const password = ref('password');

const handleSubmit = () => {
    const editUserData = {
        id: props.user.id,
        email: email.value,
        username: username.value,
        passwd: password.value
    };

    const createUserData = {
        email: email.value,
        username: username.value,
        passwd: password.value
    };

    const sendRequest = (method: 'PUT' | 'POST', userData: any, errorMessage: string) => {
        return fetch(`http://localhost:5000/user/`, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(errorMessage);
            }
            return response.json();
        })
        .finally(() => {
            resetForm();
        })
        .catch(error => {
            console.error(errorMessage, error);
            throw error;
        });
    };

    if (props.editMode) {
        sendRequest('PUT', editUserData, 'Error updating user');
    } else {
        sendRequest('POST', createUserData, 'Error creating user');
    }
}

onMounted(() => {
    if (props.editMode) {
        email.value = props.user.email;
        username.value = props.user.username;
        password.value = props.user.passwd;
    } else {
        resetForm();
    }
});
</script>
