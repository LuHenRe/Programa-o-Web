from app.domain.repositories.post_repository import PostRepository

class DeletePostUseCase:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
    
    def execute(self, id: str) -> None:
        self.post_repository.delete_post(id)
