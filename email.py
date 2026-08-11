import re

class Email:
    def __init__(self, value: str) -> None:
        if not self._is_valid():
            raise ValueError("Email inválido")
        self.value = value

    def _is_valid(self, email: str) -> bool:
        pattern = r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$"
        return re.match(pattern, email) is not None

    def _eq_(self, other) -> bool:
        return isinstance(other, Email) and self.value == other.value

    def __str__(self) -> str:
        return self.value