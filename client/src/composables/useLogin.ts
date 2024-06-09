import { ref } from "vue";
import ApiService from "@/services/api";
import { useStore } from "vuex";
import router from "@/router";

export default function useLogin() {
  const store = useStore();
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const login = async (email: string, password: string) => {
    if (!email || !password) {
      error.value = "Please enter the email and password";
      return;
    }
    isLoading.value = true;
    error.value = null;
    try {
      const response = await ApiService.login({ email, passwd: password });
      store.dispatch("login", {
        token: response.data.token,
        role: response.data.user.role,
      });
      router.push("/")
    } catch (err: any) {
      error.value =
        err.message ?? "Credentials are incorrect. Please try again";
    } finally {
      isLoading.value = false;
    }
  };

  return { isLoading, error, login };
}
