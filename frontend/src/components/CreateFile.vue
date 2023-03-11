<template>
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <form
      @submit.prevent="uploadFile"
      class="mx-auto mt-8 mb-0 max-w-md space-y-4"
    >
      <div>
        <label for="file" class="sr-only">File to upload</label>

        <div class="relative">
          <input
            ref="fileInput"
            type="file"
            name="s3_name"
            class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
          />
          <input
            ref="sampleName"
            type="text"
            name="sample_name"
            value="samplename"
            class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
          />
          <input
            ref="sampleBpm"
            type="text"
            name="bpm"
            value="bpm"
            class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
          />
          <input
            ref="sampleKey"
            type="text"
            name="key"
            value="key"
            class="w-full rounded-lg border-gray-200 p-4 pr-12 text-sm shadow-sm"
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
    uploadFile() {
      const file = this.$refs.fileInput.files[0];
      const reader = new FileReader();
      reader.onloadend = () => {
        const fileData = new Blob([reader.result], { type: file.type });
        const formData = new FormData();
        const extension = file.name.split(".").pop();
        formData.append("sample_name", this.$refs.sampleName.value);
        formData.append("sample_bpm", this.$refs.sampleBpm.value);
        formData.append("sample_key", this.$refs.sampleKey.value);
        formData.append("sample_owner", "testing");
        formData.append(
          "s3_name",
          fileData,
          this.$refs.sampleName.value +
            this.$refs.sampleBpm.value +
            this.$refs.sampleKey.value +
            "testing" +
            "." +
            extension
        );

        for (const [key, value] of formData.entries()) {
          console.log(`${key}: ${value}`);
        }
        const uploadPromise = new Promise((resolve, reject) => {
          axios
            .post("http://127.0.0.1:5000/upload", formData)
            .then((response) => {
              resolve(response);
            })
            .catch((error) => {
              reject(error);
            });
        });
        uploadPromise
          .then((response) => {
            console.log(response);
            // do something with the response
          })
          .catch((error) => {
            console.log(error);
            // handle the error
          });
      };
      reader.readAsArrayBuffer(file);
    },
  },
};
</script>
