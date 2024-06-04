import { ref, computed } from 'vue';
import ApiService from '@/services/api';

interface PredictionResponse {
  'Deformed cells detected': number;
  'Healthy cells detected': number;
  annotatedImage: { data: string }; // Base64 encoded image data
}

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