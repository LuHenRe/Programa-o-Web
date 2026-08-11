class Password:
    def __init__(self, value: str) -> None:
        if not self._is_valid():
            raise ValueError("Senha inválida")
        self.value = value

    def _is_valid(self, password: str) -> bool:
        return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password))

    def _eq_(self, other) -> bool:
        return isinstance(other, Password) and self.value == other.value

    def __str__(self) -> str:
        return "*" * len(self.value)