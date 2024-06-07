import { ref } from 'vue';
import ApiService from '@/services/api';

export default function useLogin() {
  const user = ref<object | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const login = async (email: string, password: string) => {
    if(!email || !password) {
      error.value = "Please enter the email and password"
      return
    }
    isLoading.value = true;
    error.value = null;
    try {
      const response = await ApiService.login({email, passwd: password});
      user.value = response;
    } catch (err: any) {
      error.value = err.message ?? 'Credentials are incorrect. Please try again';
    } finally {
      isLoading.value = false;
    }
  };

  return { user, isLoading, error, login };
}