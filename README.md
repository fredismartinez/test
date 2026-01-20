# Obsidian-like (Vue + Python)

Este repositorio contiene un prototipo modular inspirado en Obsidian con:

- Backend en Python (FastAPI) para gestionar vaults, notas y render de Markdown.
- Frontend en Vue 3 para edición, vista previa y enlaces tipo `[[wiki]]`.

## Estructura

- `backend/`: API de vaults, notas, configuración y render de Markdown.
- `frontend/`: UI en Vue con editor y preview.
- `data/`: almacenamiento de vaults y notas.

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

La UI espera que el backend corra en `http://localhost:8000`.
