<template>
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <form
      @submit.prevent="uploadText"
      class="mx-auto mt-8 mb-0 max-w-md space-y-4"
    >
      <div>
        <label for="text" class="sr-only">Text to upload</label>

        <div class="relative">
          <input
            v-model="text"
            type="text"
            class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
            placeholder="Enter text to upload"
          />
        </div>
      </div>

      <div class="flex items-center justify-center">
        <button
          type="submit"
          class="inline-block rounded-lg bg-blue-500 px-5 py-3 text-sm font-medium text-white"
        >
          Upload
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      text: "",
    };
  },
  methods: {
    uploadText() {
      const formData = new FormData();
      formData.append("filename", this.text);

      axios
        .post("http://127.0.0.1:5000/upload", formData)
        .then((response) => {
          console.log(response);
          // do something with the response
        })
        .catch((error) => {
          console.log(error);
          // handle the error
        });
    },
  },
};
</script>
