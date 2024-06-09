<script setup lang="ts">
import store from "@/store";
import { ref, watch } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const toggledButton = ref<string | null>(null);

watch(
  () => router.currentRoute.value.name,
  (newName) => {
    if (newName) toggledButton.value = newName.toString();
  },
  { immediate: true }
);

const toggleButton = (button: string) => {
  router.push({ name: button });
};

const logout = () => {
  store.dispatch("logout");
  location.reload();
};
</script>

<template>
  <nav class="flex bg-transparent font-bold justify-between p-3">
    <router-link :to="{ name: 'RBCDetection' }" class="text-xl text-white">
      Healthy and Deformed Cells AI Detection
    </router-link>
    <div class="text-white flex space-x-2">
      <button
        :class="[
          'rounded rounded-2xl p-2',
          toggledButton === 'RBCDetection'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('RBCDetection')"
      >
        RBC Detection
      </button>
      <button
        :class="[
          'rounded rounded-2xl p-2',
          toggledButton === 'Comparison'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('Comparison')"
      >
        RBC Image Comparison
      </button>

      <button
        v-if="store.getters.getRole == 'ADMIN'"
        :class="[
          'rounded-2xl p-2',
          toggledButton === 'Admin'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('Admin')"
      >
        Admin Dashboard
      </button>

      <button
        v-if="store.getters.getToken"
        :class="['rounded-2xl p-2 bg-red-500 text-white']"
        @click="logout"
      >
        Logout
      </button>
      <button
        v-else
        :class="[
          'rounded rounded-2xl p-2',
          toggledButton === 'Login'
            ? 'bg-white text-black'
            : 'bg-gray-400 text-white',
        ]"
        @click="toggleButton('Login')"
      >
        Login
      </button>
    </div>
  </nav>
</template>

<style scoped></style>
