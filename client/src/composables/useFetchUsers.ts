import { ref } from "vue";
import ApiClient from "@/services/api";
 
interface User {
  id: number;
  email: string;
  username: string;
  passwd: string;
}

export function useFetchUsers() {
  const users = ref<User[]>([]);
  const fetchUserError = ref<string | null>(null);

  const fetchUsers = async () => {
    fetchUserError.value = null;

    try {
      const response = await ApiClient.fetchUsers();
      users.value = response.users;
      console.log(users.value);
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
