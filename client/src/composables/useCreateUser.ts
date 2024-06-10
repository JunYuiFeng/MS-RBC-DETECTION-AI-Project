import { ref } from 'vue';
import ApiService from '@/services/api';

interface CreateUserData {
    email: string;
    username: string;
    passwd: string;
}

export function useCreateUser() {
  const createUserError = ref<string | null>(null);

  const createUser = async (createUserData: CreateUserData) => {
    // Check if all required fields are provided
    if (
      !createUserData.email ||
      !createUserData.username ||
      !createUserData.passwd
    ) {
      createUserError.value = 'Please enter the email, username, and password';
      return;
    }

    createUserError.value = null; // Reset error message

    try {
      await ApiService.createUser(createUserData);
    } catch (err: any) {
      // Handle any other errors (network issues, etc.)
      createUserError.value = err.message || 'Failed to create user';
    }
  };

  return { createUserError, createUser };
}