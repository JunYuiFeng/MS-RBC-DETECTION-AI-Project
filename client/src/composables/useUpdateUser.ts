import { ref } from 'vue';
import ApiService from '@/services/api';

interface User {
    id: number;
    email: string;
    username: string;
    passwd: string;
}

export function useUpdateUser() {
    const updateUserError = ref<string | null>(null);
    
    const updateUser = async (user: User) => {
        if (!user.email || !user.username || !user.passwd) {
            updateUserError.value = 'Please enter the email, username, and password';
            return;
        }

        updateUserError.value = null;

        const response = await ApiService.updateUser(user);
        // console.log(response.data);
        
        if (response.status !== 200) {
            // console.log(response.data);
            
            updateUserError.value = response.data.error;
            console.log(updateUserError.value);
            
        } else {
          return;
        }
    };
    
    return { updateUserError, updateUser };
}
