<template>
    <div class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-50">
        <div class="text-left bg-white p-5 rounded-xl w-1/3">
            <div>
                <div class="mb-4">
                    <label class="block text-gray-700">Email:</label>
                    <input v-model="email" type="email" class="w-full px-3 py-2 border rounded" required/>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Username:</label>
                    <input v-model="username" type="text" class="w-full px-3 py-2 border rounded" required/>
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700">Password:</label>
                    <input v-model="password" type="password" class="w-full px-3 py-2 border rounded" required/>
                </div>
                <div v-if="errorMessage" id="errorLabel" class="border border-red-400 rounded bg-red-100 px-4 py-3 mb-5 text-red-700 fade">{{ errorMessage }}</div>    
                <div class="flex justify-end gap-4">
                    <button @click="emit('close')" type="button" class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded">Cancel</button>
                    <button @click="handleSubmit" class="bg-green-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Confirm</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref, onMounted } from 'vue';
import { useCreateUser } from '@/composables/useCreateUser';
import { useUpdateUser } from '@/composables/useUpdateUser';
import { useFetchUsers } from '@/composables/useFetchUsers';

const email = ref('email');
const username = ref('username');
const password = ref('password');
const emit = defineEmits(['close', 'confirm']);
const { createUser, createUserError } = useCreateUser();
const { updateUser, updateUserError } = useUpdateUser();
const { fetchUsers, users, fetchUserError } = useFetchUsers();
const errorMessage = ref<string | null>(null);

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


const validateEmail = (email: string) => {
    const isValid = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email);
    return isValid;
};


const handleSubmit = async () => {
    if (!email.value || !username.value || !password.value) {
        showErrorLabel('Please fill in all fields');
        return;
    }

    if (!validateEmail(email.value)) {
        showErrorLabel('Please enter a valid email address');
        return;
    }

    if (props.editMode) {
        // Check for duplicates excluding the current user
        for (const user of users.value) {
            if (user.id !== props.user.id) {
                if (user.email === email.value) {
                    showErrorLabel('Email already exists');
                    return;
                }

                if (user.username === username.value) {
                    showErrorLabel('Username already exists');
                    return;
                }
            }
        }

        const editUserData = {
            id: props.user.id,
            email: email.value,
            username: username.value,
            passwd: password.value
        };

        await updateUser(editUserData);

        if (!updateUserError.value) {
            resetForm();
            emit('confirm');
        } else {
            showErrorLabel(updateUserError.value);
        }
    } else {

        for (const user of users.value) {
            if (user.email === email.value) {
                showErrorLabel('Email already exists');
                return;
            }

            if (user.username === username.value) {
                showErrorLabel('Username already exists');
                return;
            }
        }

        const createUserData = {
            email: email.value,
            username: username.value,
            passwd: password.value
        };

        await createUser(createUserData);

        if (!createUserError.value) {
            resetForm();
            emit('confirm');
        } else {
            showErrorLabel(createUserError.value);
        }
    }
}

const showErrorLabel = (message: any) => {
    errorMessage.value = message;
}

onMounted(() => {
    if (props.editMode) {
        email.value = props.user.email;
        username.value = props.user.username;
        password.value = props.user.passwd;
    } else {
        resetForm();
    }

    fetchUsers();
    if (fetchUserError.value) {
        showErrorLabel('Error fetching users');
    }
});
</script>
