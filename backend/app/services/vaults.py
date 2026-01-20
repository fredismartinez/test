from pathlib import Path

from app.config import DEFAULT_CONFIG, VAULTS_DIR
from app.storage import ensure_dir, read_json, write_json


def list_vaults() -> list[dict]:
    ensure_dir(VAULTS_DIR)
    vaults = []
    for vault_path in sorted(VAULTS_DIR.iterdir()):
        if not vault_path.is_dir():
            continue
        notes_dir = vault_path / "notes"
        note_count = len(list(notes_dir.rglob("*.md"))) if notes_dir.exists() else 0
        vaults.append(
            {
                "name": vault_path.name,
                "path": str(vault_path),
                "note_count": note_count,
            }
        )
    return vaults


def create_vault(name: str) -> dict:
    vault_path = VAULTS_DIR / name
    notes_path = vault_path / "notes"
    config_path = vault_path / "config.json"
    ensure_dir(notes_path)
    if not config_path.exists():
        write_json(config_path, DEFAULT_CONFIG)
    return {
        "name": name,
        "path": str(vault_path),
        "note_count": 0,
    }


def get_config(vault_name: str) -> dict:
    return read_json(VAULTS_DIR / vault_name / "config.json")


def update_config(vault_name: str, payload: dict) -> dict:
    config_path = VAULTS_DIR / vault_name / "config.json"
    current = read_json(config_path)
    current.update(payload)
    write_json(config_path, current)
    return current
