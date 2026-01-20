<template>
  <div class="app-shell">
    <aside class="sidebar">
      <header>
        <h1>Vaults</h1>
        <div class="vault-actions">
          <input v-model="newVault" placeholder="Nuevo vault" />
          <button @click="handleCreateVault">Crear</button>
        </div>
      </header>
      <ul class="vault-list">
        <li v-for="vault in vaults" :key="vault.name">
          <button
            :class="{ active: vault.name === activeVault }"
            @click="selectVault(vault.name)"
          >
            <span>{{ vault.name }}</span>
            <small>{{ vault.note_count }} notas</small>
          </button>
        </li>
      </ul>
      <div v-if="activeVault" class="notes">
        <h2>Notas</h2>
        <ul>
          <li v-for="note in notes" :key="note.path">
            <button
              :class="{ active: note.path === activeNote?.path }"
              @click="openNote(note.path)"
            >
              {{ note.title }}
            </button>
          </li>
        </ul>
      </div>
    </aside>

    <main class="editor">
      <div v-if="!activeVault" class="empty">
        <p>Selecciona o crea un vault para comenzar.</p>
      </div>
      <div v-else class="workspace">
        <header class="workspace-header">
          <input
            v-model="noteTitle"
            placeholder="Título de nota"
            class="title-input"
          />
          <button @click="saveActiveNote">Guardar</button>
        </header>
        <section class="workspace-body">
          <textarea v-model="noteContent" class="editor-input"></textarea>
          <div class="preview" v-html="renderedHtml"></div>
        </section>
        <footer class="workspace-footer">
          <span>Enlaces detectados:</span>
          <div class="link-chips">
            <span v-for="link in activeLinks" :key="link" class="chip">{{ link }}</span>
          </div>
        </footer>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { api } from "./api";

const vaults = ref([]);
const notes = ref([]);
const activeVault = ref("");
const activeNote = ref(null);
const newVault = ref("");

const noteTitle = ref("");
const noteContent = ref("");
const renderedHtml = ref("");
const activeLinks = ref([]);

const loadVaults = async () => {
  vaults.value = await api.listVaults();
};

const selectVault = async (vaultName) => {
  activeVault.value = vaultName;
  notes.value = await api.listNotes(vaultName);
  activeNote.value = null;
  noteTitle.value = "";
  noteContent.value = "";
  renderedHtml.value = "";
  activeLinks.value = [];
};

const handleCreateVault = async () => {
  if (!newVault.value.trim()) return;
  await api.createVault(newVault.value.trim());
  newVault.value = "";
  await loadVaults();
};

const openNote = async (notePath) => {
  if (!activeVault.value) return;
  const note = await api.readNote(activeVault.value, notePath);
  activeNote.value = note;
  noteTitle.value = note.title;
  noteContent.value = note.content;
  activeLinks.value = note.links;
  await updatePreview(note.content);
};

const saveActiveNote = async () => {
  if (!activeVault.value || !noteTitle.value.trim()) return;
  const payload = {
    title: noteTitle.value.trim(),
    content: noteContent.value,
  };
  await api.saveNote(activeVault.value, payload);
  notes.value = await api.listNotes(activeVault.value);
  await openNote(`${payload.title}.md`);
};

const updatePreview = async (content) => {
  const response = await api.renderMarkdown(content);
  renderedHtml.value = response.html;
};

watch(noteContent, async (value) => {
  if (!activeVault.value) return;
  await updatePreview(value);
});

onMounted(loadVaults);
</script>
