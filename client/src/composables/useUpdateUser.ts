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
        try {
        await ApiService.updateUser(user);
        } catch (err: any) {
            updateUserError.value = err.message ?? 'Failed to update user';
        }
    };
    
    return { updateUserError, updateUser };
}
