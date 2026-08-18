from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    title: str = Field(min_length=5, max_length=255, description="Título do post")
    content: str = Field(min_length=10, max_length=1000, description="Conteúdo do post")
