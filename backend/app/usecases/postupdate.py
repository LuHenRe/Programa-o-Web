from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class UpdatePostUseCase:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post: Post) -> Post:
        self.post_repository.update(post)
        return post
