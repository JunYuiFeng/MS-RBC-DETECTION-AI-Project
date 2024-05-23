<template>
    <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
        <NavBar />
    </div>
    <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600">


        <div class="bg-white p-10 w-1/2 rounded-3xl">
            <div class="text-2xl font-black flex justify-start mb-5">Upload one or more images</div>
            <div class="grid grid-cols-12 gap-1">
                <div class="col-span-8">
                    <div class="flex items-center justify-center w-full">
                        <label for="dropzone-file"
                            class="flex flex-col items-center justify-center w-full h-64 border-2 border-violet-900 border-dashed rounded-lg cursor-pointer bg-white">
                            <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                                </svg>
                                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span
                                        class="font-semibold">Click to upload</span> or drag and drop</p>
                                <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX.
                                    800x400px)</p>
                            </div>
                            <input id="dropzone-file" type="file" class="hidden" />
                        </label>
                    </div>
                </div>
                <div class="col-span-4 flex items-end justify-end">
                    <button
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded bg-indigo-950 text-sm rounded-xl">Detect
                        RBC</button>
                </div>
            </div>
        </div>

        <!-- <div class="text-white">No images?</div> -->
    </div>
</template>

<script setup lang="ts">
import NavBar from '/src/components/NavBar.vue'

</script>

<style scoped></style>