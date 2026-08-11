from app.domain.repositories.user_repository import UserRepository

class LogoutUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def execute(self) -> None:
        self.user_repository.logout()