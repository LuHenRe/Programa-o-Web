from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class CreatePostUseCase:
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def execute(self, post: Post) -> None:
        self.post_repository.create(post)