from classes.user import User, UserAlreadyExistsError, UserNotFoundError
from classes.userManager import UserManager


def main():
    manager = UserManager()

    print("=" * 60)
    print("1. Добавление пользователей (включая дубликаты)")
    print("=" * 60)

    users_to_add = [
        User("alice", "alice@example.com", 25),
        User("bob", "bob@example.com", 30),
        User("alice", "alice2@example.com", 26),  # дубликат
        User("charlie", "charlie@example.com", 22),
        User("bob", "bob2@example.com", 31),      # дубликат
    ]

    for user in users_to_add:
        try:
            manager.add_user(user)
        except UserAlreadyExistsError as e:
            print(f"[ERROR] {e}")

    print("\n" + "=" * 60)
    print("2. Удаление пользователей (включая отсутствующих)")
    print("=" * 60)

    usernames_to_remove = ["alice", "dave", "bob", "eve"]

    for username in usernames_to_remove:
        try:
            manager.remove_user(username)
        except UserNotFoundError as e:
            print(f"[ERROR] {e}")

    print("\n" + "=" * 60)
    print("3. Поиск пользователей (включая отсутствующих)")
    print("=" * 60)

    usernames_to_find = ["charlie", "alice", "bob", "zoe"]

    for username in usernames_to_find:
        try:
            user = manager.find_user(username)
            print(f"[OK] Найден: {user}")
        except UserNotFoundError as e:
            print(f"[ERROR] {e}")

    print("\n" + "=" * 60)
    print("Итоговое состояние менеджера:")
    print("=" * 60)
    if manager.users:
        for u in manager.users.values():
            print(f"  {u}")
    else:
        print("  (пусто)")


if __name__ == "__main__":
    main()