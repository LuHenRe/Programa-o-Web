from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class GetAllPostsUseCase:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
    
    def execute(self) -> list[Post]:
        return self.post_repository.get_all_posts()
