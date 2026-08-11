from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def create(self, user: User) -> None:
        self.users.append(user)

    def get_all(self) -> list[User]:
        return self.users

    def get_by_id(self, id: str) -> User | None:
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update(self, user: User) -> None:
        for user in self.users:
            if user.id == user.id:
                user.email = user.email
                user.password = user.password
                return

    def delete(self, id: str) -> None:
        for user in self.users:
            if user.id == id:
                self.users.remove(user)
                return