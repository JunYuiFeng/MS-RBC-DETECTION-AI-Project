import { ref } from "vue";
import ApiService, { UserResponse } from "@/services/api";

export function useFetchUsers() {
  const users = ref<UserResponse[]>([]);
  const fetchUserError = ref<string | null>(null);

  const fetchUsers = async () => {
    fetchUserError.value = null;

    try {
      const response = await ApiService.fetchUsers();
      users.value = response.users;
    } catch (err: any) {
      fetchUserError.value = err.message;
    } 
  };

  return {
    users,
    fetchUserError,
    fetchUsers,
  };
}
