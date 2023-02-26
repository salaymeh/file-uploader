<template>
  <section class="lg:mx-auto lg:max-w-screen-sm lg:py-10">
    <div class="bg-white">
      <NavBar class="lg:mt-10 lg:mb-4 sm:mt-2 sm:ml-2 sm:mr-2 sm:mb-2"></NavBar>
      <main>
        <router-view></router-view>
      </main>
    </div>
  </section>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  components: {
    NavBar,
  },
};
</script>
