<template>
  <div class="flex items-center justify-center">
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>FileName</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="file in files" :key="file.id">
          <td class="border px-4 py-2">{{ file.id }}</td>
          <td class="border px-4 py-2">{{ file.filename }}</td>
          <td class="border px-4 py-2">
            <button
              class="border px-4 py-2 bg-gray-300"
              @click="deleteFile(file.id)"
            >
              Delete
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
              filename: data[id].filename,
            });
          }
          this.files = results;
        })
        .catch((error) => {
          console.log(error);
          this.error = "failed to fetch data";
        });
    },
    deleteFile(id) {
      axios
        .delete(`http://127.0.0.1:5000/files/delete/${id}`)
        .then((response) => {
          console.log(response);
          // Reload the files after deleting a file
          this.loadFiles();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.loadFiles();
  },
};
</script>
