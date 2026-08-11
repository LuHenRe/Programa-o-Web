from backend.app.domain.entities.post import Post
from abc import ABC, abstractmethod

class PostRepository(ABC):
    @abstractmethod
    def create_post(self, post: Post) -> None:
        pass

    @abstractmethod
    def update_post(self, post: Post) -> None:
        pass

    @abstractmethod
    def delete_post(self, post: Post) -> None:
        pass

    @abstractmethod
    def get_all_posts(self) -> list[Post]:
        pass

    @abstractmethod
    def get_post_by_id(self, id: str) -> Post | None:
        pass