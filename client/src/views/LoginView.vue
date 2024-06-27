<script setup lang="ts">
import LoadingSpinner from "@/components/LoadingSpinner.vue";
import useLogin from "@/composables/useLogin";
import { ref } from "vue";

const { login, isLoading, error } = useLogin();

const email = ref("");
const password = ref("");

// Login button click event
function onSignInBtnClick() {
  login(email.value, password.value);
}
</script>

<style scoped></style>
<template>
  <div class="flex items-start justify-center">
    <div
      class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
    >
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img
          class="mx-auto h-10 w-auto"
          src="@/assets/rr-logo.png"
          alt="RR Mechatronics"
        />
        <h2
          class="mt-5 text-center text-2xl font-bold leading-9 tracking-tight text-white"
        >
          Sign in to your account
        </h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div>
          <div class="flex items-center justify-between">
            <label
              for="email"
              class="block text-sm font-medium leading-6 text-white"
              >Email address</label
            >
          </div>
          <div class="mt-2">
            <input
              name="email"
              type="email"
              v-model="email"
              autocomplete="email"
              class="block p-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div class="mt-5">
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-white"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              name="password"
              type="password"
              autocomplete="current-password"
              v-model="password"
              class="block p-2 w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div v-if="error" class="text-red-500 mt-3">{{ error }}</div>

        <div class="mt-5">
          <button
            type="submit"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            @click="onSignInBtnClick"
          >
            {{ !isLoading ? "Sign in" : "" }}
            <LoadingSpinner v-if="isLoading" />
          </button>
        </div>

        <p class="mt-10 text-center text-sm text-gray-300">
          Not a member? Ask the administrator to create an account for you
        </p>
      </div>
    </div>
  </div>
</template>
