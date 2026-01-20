from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import NotePayload, VaultCreate
from app.services.markdown import render_markdown
from app.services.notes import list_notes, read_note, save_note
from app.services.vaults import create_vault, get_config, list_vaults, update_config

app = FastAPI(title="Obsidian-Like Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok"}


@app.get("/vaults")
async def vaults_index() -> list[dict]:
    return list_vaults()


@app.post("/vaults")
async def vaults_create(payload: VaultCreate) -> dict:
    return create_vault(payload.name)


@app.get("/vaults/{vault_name}/config")
async def vault_config(vault_name: str) -> dict:
    config = get_config(vault_name)
    if not config:
        raise HTTPException(status_code=404, detail="Vault config not found")
    return config


@app.put("/vaults/{vault_name}/config")
async def vault_config_update(vault_name: str, payload: dict) -> dict:
    return update_config(vault_name, payload)


@app.get("/vaults/{vault_name}/notes")
async def notes_index(vault_name: str) -> list[dict]:
    return list_notes(vault_name)


@app.get("/vaults/{vault_name}/notes/{note_path:path}")
async def notes_detail(vault_name: str, note_path: str) -> dict:
    return read_note(vault_name, note_path)


@app.post("/vaults/{vault_name}/notes")
async def notes_save(vault_name: str, payload: NotePayload) -> dict:
    return save_note(vault_name, payload.title, payload.content, payload.folder)


@app.post("/markdown/render")
async def markdown_render(payload: dict) -> dict:
    content = payload.get("content", "")
    return {"html": render_markdown(content)}
