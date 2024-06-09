import { ref } from 'vue';
import ApiService from '@/services/api';

interface User {
    id: number;
    email: string;
    username: string;
    passwd: string;
}

export default function useUpdateUser() {
    const updateUserError = ref<string | null>(null);
    
    const updateUser = async (id: number, email: string, username: string, passwd: string) => {
        if (!email || !username || !passwd) {
            updateUserError.value = 'Please enter the email, username, and password';
            return;
        }

        const user: User = { id, email, username, passwd };
        updateUserError.value = null;
        try {
        await ApiService.updateUser(user);
        } catch (err: any) {
            updateUserError.value = err.message ?? 'Failed to update user';
        }
    };
    
    return { updateUserError, updateUser };
}
