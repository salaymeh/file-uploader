<template>
  <div class="flex items-center justify-center">
    <table>
      <thead>
        <tr>
          <th>Sample</th>
          <th>BPM</th>
          <th>Key</th>
          <th>Author</th>
          <th>Download</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="file in files" :key="file.id">
          <!-- <td class="border px-4 py-2">{{ file.id }}</td> -->
          <td class="border px-4 py-2">{{ file.sampleName }}</td>
          <td class="border px-4 py-2">{{ file.sampleBpm }}</td>
          <td class="border px-4 py-2">{{ file.sampleKey }}</td>
          <td class="border px-4 py-2">{{ file.sampleOwner }}</td>
          <td class="border px-4 py-2">
            <button
              class="border px-4 py-2 bg-gray-300"
              @click="redirectToUrl(file.url)"
            >
              download
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      files: [],
    };
  },
  methods: {
    loadFiles() {
      axios
        .get("http://127.0.0.1:5000/files")
        .then((response) => {
          const data = response.data;
          const results = [];
          for (const id in data) {
            results.push({
              id: data[id].id,
              sampleName: data[id].sample_name,
              sampleBpm: data[id].sample_bpm,
              sampleKey: data[id].sample_key,
              sampleOwner: data[id].sample_owner,
              url: data[id].url,
            });
          }
          this.files = results;
        })
        .catch((error) => {
          console.log(error);
          this.error = "failed to fetch data";
        });
    },
    redirectToUrl(url) {
      window.location.href = url;
    },
  },
  mounted() {
    this.loadFiles();
  },
};
</script>
