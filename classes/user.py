class UserError(Exception):
    """Базовый класс для всех ошибок, связанных с пользователями."""
    pass


class UserAlreadyExistsError(UserError):
    """Выбрасывается при попытке добавить пользователя с существующим именем."""
    def __init__(self, username: str):
        self.username = username
        super().__init__(f"Пользователь с именем '{username}' уже существует.")


class UserNotFoundError(UserError):
    """Выбрасывается, если пользователь с указанным именем не найден."""
    def __init__(self, username: str):
        self.username = username
        super().__init__(f"Пользователь с именем '{username}' не найден.")


class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self) -> str:
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"

    def __repr__(self) -> str:
        return self.__str__()



