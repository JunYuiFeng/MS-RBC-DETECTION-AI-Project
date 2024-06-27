import { ref } from 'vue';
import ApiService, { CreateUserData } from '@/services/api';

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
    const response = await ApiService.createUser(createUserData);

    if (response.status !== 200) {
      createUserError.value = response?.data?.error;
    } else {
      return
    }
  };

  return { createUserError, createUser };
}