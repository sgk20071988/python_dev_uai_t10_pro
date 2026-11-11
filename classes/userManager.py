from classes.user import User, UserAlreadyExistsError, UserNotFoundError


class UserManager:
    def __init__(self):
        self.users: dict[str, User] = {}

    def add_user(self, user: User) -> None:
        """Добавляет пользователя. Если имя занято — UserAlreadyExistsError."""
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user
        print(f"[OK] Добавлен пользователь: {user}")

    def remove_user(self, username: str) -> None:
        """Удаляет пользователя. Если его нет — UserNotFoundError."""
        if username not in self.users:
            raise UserNotFoundError(username)
        removed = self.users.pop(username)
        print(f"[OK] Удалён пользователь: {removed}")

    def find_user(self, username: str) -> User:
        """Возвращает пользователя. Если его нет — UserNotFoundError."""
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]