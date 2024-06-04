<template>
  <div class="bg-gradient-to-r from-violet-900 to-indigo-600">
    <NavBar />
  </div>
  <div
    class="flex items-start justify-center min-h-screen bg-gradient-to-r from-violet-900 to-indigo-600"
  >
    <div
      class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
    >
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img
          class="mx-auto h-10 w-auto"
          src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
          alt="Your Company"
        />
        <h2
          class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
        >
          Sign in to your account
        </h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <div class="space-y-6">
          <div>
            <div class="flex items-center justify-between">
              <label
                for="email"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Email address</label
              >
            </div>
            <div class="mt-2">
              <input
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label
                for="password"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Password</label
              >
            </div>
            <div class="mt-2">
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              @click="login"
            >
              Sign in
            </button>
          </div>
          <div v-if="showErrorLabel" role="alert">
            <div class="bg-red-500 text-white font-bold rounded px-4 py-2">
              Error: Incorrect credentials
            </div>
          </div>
        </div>

        <p class="mt-10 text-center text-sm text-gray-500">
          Not a member? Ask the administrator to create an account for you
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import NavBar from "/src/components/NavBar.vue";
import { ref } from "vue";

const showErrorLabel = ref(false);

const email = ref("email");
const password = ref("password");

const login = async () => {
  const response = await fetch("http://localhost:5000/auth", {
    method: "POST",
    body: JSON.stringify({ email: email, passwd: password}),
    headers: { "Content-Type": "application/json" },
  });

  if (response.ok) {
    console.log("Login successful");
  } else {
    showErrorLabel.value = true;
  }
};
</script>

<style scoped>
h2 {
  color: white;
}

label {
  color: white;
}

p {
  color: white;
  opacity: 0.8;
}
</style>
