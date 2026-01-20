import axios from "axios";

const client = axios.create({
  baseURL: "http://localhost:8000",
});

export const api = {
  async listVaults() {
    const { data } = await client.get("/vaults");
    return data;
  },
  async createVault(name) {
    const { data } = await client.post("/vaults", { name });
    return data;
  },
  async listNotes(vaultName) {
    const { data } = await client.get(`/vaults/${vaultName}/notes`);
    return data;
  },
  async readNote(vaultName, notePath) {
    const { data } = await client.get(`/vaults/${vaultName}/notes/${notePath}`);
    return data;
  },
  async saveNote(vaultName, payload) {
    const { data } = await client.post(`/vaults/${vaultName}/notes`, payload);
    return data;
  },
  async renderMarkdown(content) {
    const { data } = await client.post("/markdown/render", { content });
    return data;
  },
};
