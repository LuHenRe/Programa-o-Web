from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User
from fastapi import HTTPException

class RegisterUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self, user: User) -> None:
        if self.user_repository.get_by_email(user, email):
            raise HTTPException(status_code=400, detail="Email já cadastrado")
        self.user_repository.create(user)
