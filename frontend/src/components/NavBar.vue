<template>
  <header aria-label="Site Header" class="bg-white border border-gray-800">
    <div
      class="lg:mx-auto lg:max-w-screen-xl lg:px-8 md:mx-auto lg:max-w-screen-l"
    >
      <div class="flex h-16 items-center justify-between">
        <div
          class="lg:flex md:flex lg:items-center lg:gap-12 md:items-center md:gap-12"
        ></div>
        <div class="md:block m-auto">
          <nav aria-label="Site Nav">
            <ul class="flex items-center gap-6 text-sm sm:gap-4">
              <li>
                <router-link
                  to="/main"
                  class="text-black-500 transition hover:text-gray-500/75"
                >
                  Home
                </router-link>
              </li>
              <li>
                <router-link
                  to="/create"
                  class="text-black-500 transition hover:text-gray-500/75"
                >
                  Create
                </router-link>
              </li>
              <li>
                <router-link
                  to="/update"
                  class="text-black-500 transition hover:text-gray-500/75"
                >
                  Update
                </router-link>
              </li>
              <li>
                <router-link
                  to="/delete"
                  class="text-black-500 transition hover:text-gray-500/75"
                >
                  Delete
                </router-link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.mobile {
  margin: 10px;
}
</style>
