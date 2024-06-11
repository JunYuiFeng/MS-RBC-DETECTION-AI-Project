import { ref, computed } from 'vue';
import ApiService, { ComparisonResponse } from '@/services/api';

export default function usePredictMultipleAndCompare() {
  const comparison = ref<ComparisonResponse | null>(null);
  const isLoading = ref(false);
  const error = ref<string | null>(null);

  const predictMultipleAndCompare = async (patient1Images: File[], patient2Images: File[]) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await ApiService.compare(patient1Images, patient2Images);
      comparison.value = response;
    } catch (err) {
      console.error('Error comparing images:', err);
      error.value = 'Error comparing images. Please try again.';
    } finally {
      isLoading.value = false;
    }
  };

  const hasComparison = computed(() => comparison.value !== null);

  return { comparison, isLoading, error, predictMultipleAndCompare, hasComparison };
}
