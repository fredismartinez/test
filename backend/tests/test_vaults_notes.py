from pathlib import Path

from app.services import notes as notes_service
from app.services import vaults as vaults_service


def test_create_vault_and_write_note(tmp_path, monkeypatch) -> None:
    vaults_dir = tmp_path / "vaults"
    monkeypatch.setattr(vaults_service, "VAULTS_DIR", vaults_dir)
    monkeypatch.setattr(notes_service, "VAULTS_DIR", vaults_dir)

    vault = vaults_service.create_vault("demo")
    assert vault["name"] == "demo"

    note = notes_service.save_note("demo", "Primera", "Hola [[Mundo]]", None)
    assert note["title"] == "Primera"
    assert note["links"] == ["Mundo"]

    note_detail = notes_service.read_note("demo", "Primera.md")
    assert note_detail["content"] == "Hola [[Mundo]]"

    notes = notes_service.list_notes("demo")
    assert len(notes) == 1

    vaults = vaults_service.list_vaults()
    assert vaults[0]["note_count"] == 1
    assert Path(vaults[0]["path"]).exists()
