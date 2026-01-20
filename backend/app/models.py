from typing import Optional
from pydantic import BaseModel, Field


class VaultCreate(BaseModel):
    name: str = Field(..., min_length=1)


class VaultInfo(BaseModel):
    name: str
    path: str
    note_count: int


class NoteInfo(BaseModel):
    title: str
    path: str
    links: list[str]


class NotePayload(BaseModel):
    title: str
    content: str
    folder: Optional[str] = None
