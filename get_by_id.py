from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class GetPostByIdUseCase:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
    
    def execute(self, id: str) -> Post | None:
        return self.post_repository.get_post_by_id(id)