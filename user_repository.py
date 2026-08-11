from entities.user import User
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def login(self, email: str, password: str) -> User | None:
        pass

    @abstractmethod
    def register(self, user: User) -> None:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def get_current_user(self) -> User | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass