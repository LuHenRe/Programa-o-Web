from __future__ import annotations

from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, Uuid
from sqlalchemy import Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.database import Base
from app.domain.entities.user import User
from app.domain.entities.post import Post
from app.domain.value_objects.email import Email
from app.domain.value_objects.password import Password

class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_entity(self) -> User:
        return User(
            id=self.id,
            email=Email(self.email),
            password=Password(self.password),
        )

    @staticmethod
    def from_entity(user: User) -> UserModel:
        return UserModel(
            id=user.id,
            email=user.email.value,
            password=user.password.value,
        )

class PostModel(Base):
    __tablename__ = "posts"
    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    def to_entity(self) -> Post:
        return Post(
            id=self.id,
            title=self.title,
            content=self.content,
        )

    @staticmethod
    def from_entity(post: Post) -> PostModel:
        return PostModel(
            id=post.id,
            title=post.title,
            content=post.content
        )
