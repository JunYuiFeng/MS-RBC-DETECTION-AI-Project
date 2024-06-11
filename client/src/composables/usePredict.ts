import { ref, computed } from 'vue';
import ApiService, { PredictionResponse } from '@/services/api';


export default function usePredict() {
  const prediction = ref<PredictionResponse | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const predictImage = async (image: File) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await ApiService.predict(image);
      prediction.value = response;
    } catch (err) {
      console.error('Error predicting image:', err);
      error.value = 'Error predicting image. Please try again.';
    } finally {
      isLoading.value = false;
    }
  };

  const hasPrediction = computed(() => prediction.value !== null);

  return { prediction, isLoading, error, predictImage, hasPrediction };
}