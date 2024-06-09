import { ref } from 'vue';
import ApiService from '@/services/api';

export default function useCreateUser() {
  const createUserError = ref<string | null>(null);

  const createUser = async (email: string, username: string, passwd: string) => {
    if (!email || !username || !passwd) {
        createUserError.value = 'Please enter the email, username, and password';
      return;
    }
    createUserError.value = null;
    try {
      await ApiService.createUser({ email, username, passwd });
    } catch (err: any) {
        createUserError.value = err.message ?? 'Failed to create user';
    }
  };

  return { createUserError, createUser };
}