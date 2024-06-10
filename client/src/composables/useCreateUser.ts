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
      const response = await ApiService.createUser(createUserData);

      // Check response status
      if (response.status === 200) {
        console.log('WE HAVE A WINNER');
        return;
      } else {
        // Handle non-200 status codes and ensure response data is checked properly
        createUserError.value =
          response.data?.error || 'Failed to create user';
      }
    } catch (err: any) {
      // Handle any other errors (network issues, etc.)
      createUserError.value = err.message || 'Failed to create user';
    }
  };

  return { createUserError, createUser };
}