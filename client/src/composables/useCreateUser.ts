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
    if (!createUserData.email || !createUserData.username || !createUserData.passwd) {
        createUserError.value = 'Please enter the email, username, and password';
      return;
    }
    createUserError.value = null;
    try {
      await ApiService.createUser(createUserData);
    } catch (err: any) {
        createUserError.value = err.message ?? 'Failed to create user';
    }
  };

  return { createUserError, createUser };
}