<template>
  <div class="flex flex-col flex-1">
    <label
      :for='"dropzone-file-" + inputName'
      class="flex flex-col items-center justify-center w-full h-64 border-2 border-violet-900 border-dashed rounded-lg cursor-pointer bg-white"
      @dragover.prevent="handleDragOver"
      @dragleave="handleDragLeave"
      @drop.prevent="handleDrop"
    >
      <div class="flex flex-col items-center justify-center pt-5 pb-6">
        <svg
          class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 20 16"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
          />
        </svg>
        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
          <span class="font-semibold">Click to upload</span> or drag and drop
        </p>
        <p class="text-xs text-gray-500 dark:text-gray-400">
          SVG, PNG, JPG or GIF (MAX. 800x400px)
        </p>
      </div>
      <input
        :name="inputName"
        :id='"dropzone-file-" + inputName'
        type="file"
        class="hidden"
        :multiple="multiple"
        accept="image/*"
        @change="handleFileChange"
      />
    </label>
    <p>{{ fileCount }} files selected</p>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, ref } from "vue";

const props = defineProps({
  multiple: {
    type: Boolean,
    default: false,
  },
  inputName: {
    type: String,
    default: "input",
  }
});

const emit = defineEmits<{
  (event: "fileSelected", files: FileList | null): void;
}>();

const fileCount = ref(0);

// File input change event
const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;
  if (files) {
    fileCount.value = files.length;
    emit("fileSelected", files);
  } else {
    fileCount.value = 0;
  }
};

// Drag and drop events
const handleDragOver = (event: DragEvent) => {
  event.preventDefault();
};

const handleDragLeave = (event: DragEvent) => {
  event.preventDefault();
};

const handleDrop = (event: DragEvent) => {
  const files = event.dataTransfer?.files;
  if (files) {
    fileCount.value = files.length;
    emit("fileSelected", files);
    const inputElement = document.getElementById(`dropzone-file-${props.inputName}`) as HTMLInputElement;
    if (inputElement) {
      const dataTransfer = new DataTransfer();
      Array.from(files).forEach(file => dataTransfer.items.add(file));
      inputElement.files = dataTransfer.files;
    }
  } else {
    fileCount.value = 0;
  }
};
</script>

<style scoped></style>
