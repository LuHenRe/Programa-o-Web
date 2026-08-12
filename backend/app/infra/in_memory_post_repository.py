from app.domain.repositories.post_repository import PostRepository
from app.domain.entities.post import Post

class InMemoryPostRepository(PostRepository):
    def __init__(self):
        self.posts = []

    def create(self, post: Post) -> None:
        self.posts.append(post)

    def get_all(self) -> list[Post]:
        return self.posts

    def get_by_id(self, id: str) -> Post | None:
        for post in self.posts:
            if post.id == id:
                return post
        return None

    def update(self, post: Post) -> None:
        for post in self.posts:
            if post.id == post.id:
                post.title = post.title
                post.content = post.content
                return

    def delete(self, id: str) -> None:
        for post in self.posts:
            if post.id == id:
                self.posts.remove(post)
                return
