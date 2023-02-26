import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";
import GetAll from "./components/GetAll.vue";
import CreateFile from "./components/CreateFile.vue";
import UpdateFile from "./components/UpdateFile.vue";
import DeleteFile from "./components/DeleteFile.vue";
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: GetAll },
    { path: "/main", component: GetAll },
    { path: "/create", component: CreateFile },
    { path: "/update", component: UpdateFile },
    { path: "/delete", component: DeleteFile },
  ],
});

const app = createApp(App);
app.use(router);
app.mount("#app");
