from pathlib import Path

from app.config import VAULTS_DIR
from app.services.links import extract_links
from app.storage import ensure_dir, read_text, write_text


def _vault_notes_dir(vault_name: str) -> Path:
    return VAULTS_DIR / vault_name / "notes"


def list_notes(vault_name: str) -> list[dict]:
    notes_dir = _vault_notes_dir(vault_name)
    ensure_dir(notes_dir)
    results = []
    for note_path in sorted(notes_dir.rglob("*.md")):
        content = read_text(note_path)
        results.append(
            {
                "title": note_path.stem,
                "path": str(note_path.relative_to(notes_dir)),
                "links": extract_links(content),
            }
        )
    return results


def read_note(vault_name: str, note_path: str) -> dict:
    notes_dir = _vault_notes_dir(vault_name)
    path = notes_dir / note_path
    content = read_text(path)
    return {
        "title": path.stem,
        "path": str(path.relative_to(notes_dir)),
        "content": content,
        "links": extract_links(content),
    }


def save_note(vault_name: str, title: str, content: str, folder: str | None) -> dict:
    notes_dir = _vault_notes_dir(vault_name)
    ensure_dir(notes_dir)
    if folder:
        path = notes_dir / folder / f"{title}.md"
    else:
        path = notes_dir / f"{title}.md"
    write_text(path, content)
    return {
        "title": title,
        "path": str(path.relative_to(notes_dir)),
        "links": extract_links(content),
    }
