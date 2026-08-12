from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class GetCurrentUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self) -> User | None:
        return self.user_repository.get_current_user()
