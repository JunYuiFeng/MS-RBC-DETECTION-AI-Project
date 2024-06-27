import { ref } from 'vue';
import ApiService, { User } from '@/services/api';

export function useUpdateUser() {
    const updateUserError = ref<string | null>(null);
    
    const updateUser = async (user: User) => {
        updateUserError.value = null;

        const response = await ApiService.updateUser(user);
        
        if (response.status !== 200) {       
            updateUserError.value = response.data.error;
            console.log(updateUserError.value);
            
        } else {
          return;
        }
    };
    
    return { updateUserError, updateUser };
}
