import { ref } from "vue";
import ApiService from "@/services/api";

export function useDeleteUser() {
  const deleteUserError = ref<string | null>(null);

  const deleteUser = async (id: number) => {
    deleteUserError.value = null;

    try {
      await ApiService.deleteUser(id);
    } catch (err: any) {
      deleteUserError.value = err.message;
    } 
  };

  return {
    deleteUserError,
    deleteUser,
  };
}