import { ref, computed } from 'vue';
import ApiService, { PredictionResponse } from '@/services/api';

export default function usePredict() {
  const prediction = ref<PredictionResponse | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const predictImages = async (images: File[]) => {  // Changed to handle multiple images
    isLoading.value = true;
    error.value = null;
    try {
      const response = await ApiService.predict(images);  // Assuming ApiService is updated to handle multiple images
      prediction.value = response;
    } catch (err) {
      console.error('Error predicting images:', err);
      error.value = 'Error predicting images. Please try again.';
    } finally {
      isLoading.value = false;
    }
  };

  const hasPrediction = computed(() => prediction.value !== null);

  return { prediction, isLoading, error, predictImages, hasPrediction };  // Changed predictImage to predictImages
}
