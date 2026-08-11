from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from fastapi import HTTPException

class LoginUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self, email: str, password: str) -> User | None:
        user = self.user_repository.get_by_email(email)
        if user is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        if user.password != password:
            raise HTTPException(status_code=401, detail="Senha incorreta")
        return user
