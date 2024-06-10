import { ref } from "vue";
import ApiClient from "@/services/api";
 
interface UserResponse {
  id: number;
  username: string;
  email: string;
  passwd: string;
  role: string;
}

export function useFetchUsers() {
  const users = ref<UserResponse[]>([]);
  const fetchUserError = ref<string | null>(null);

  const fetchUsers = async () => {
    fetchUserError.value = null;

    try {
      const response = await ApiClient.fetchUsers();
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
