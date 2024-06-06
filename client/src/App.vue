<template>
  <NavBar />
  <router-view />
</template>

<script setup lang="ts">
import "tailwindcss/tailwind.css";
import NavBar from "./components/NavBar.vue";
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  @apply bg-gradient-to-r from-violet-900 to-indigo-600;
}
</style>
