# Обработка сложных сценариев с собственными типами исключений
"""
Создаём систему управления пользователями в контексте нитернет-магазина.
1. Класс User:
- Атрибуты: username, email, age;
- Методы: __init__ для инициализации атрибутов, __str__ для вывода информации о пользователе в удобном формате.
2. Класс UserManager - менеджер пользователей, который позволяет добавлять, удалять, находить пользователей:
- Атрибут users — это словарь для хранения пользователей, где ключ - username, значение - объект класса User;
- Методы: add_user, remove_user, find_user осуществляют обозначенные действия в классе. Каждое действие 
сопровождается соответствующей проверкой и выбрасыванием исключений.
3. Пользовательские исключения:
- UserAlreadyExistsError — выбрасывается при попытке добавить пользователя с уже существующим именем;
- UserNotFoundError — выбрасывается при попытке найти или удалить отсутствующего пользователя.
4. Основная функция main:
- Тестирует функциональность добавления, удаления и поиска пользователей;
- Обрабатывает исключения, возникающие при попытке добавить уже существующих пользователей или удалить 
несуществующих.
"""

class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age
    
    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age})"

class UserManager:
    def __init__(self):
        self.users = {}  # Словарь для хранения пользователей

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(f"Пользователь с именем '{user.username}' уже существует.")
        self.users[user.username] = user

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден.")
        del self.users[username]

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден.")
        return self.users[username]

# Основная функция программы для тестирования
def main():
    user_manager = UserManager()
    
    # Попробуем добавить пользователей
    try:
        user1 = User("Alice", "alice@example.com", 30)
        user_manager.add_user(user1)
        print(f"Добавлен: {user1}")
        
        user2 = User("Bob", "bob@example.com", 25)
        user_manager.add_user(user2)
        print(f"Добавлен: {user2}")
        
        # Попытка добавить пользователя с уже существующим именем
        user3 = User("Alice", "alice2@example.com", 28)
        user_manager.add_user(user3)
    except UserAlreadyExistsError as e:
        print(e)

    # Попробуем удалить пользователей
    try:
        user_manager.remove_user("Charlie")  # Пользователь не существует
    except UserNotFoundError as e:
        print(e)

    try:
        user_manager.remove_user("Alice")  # Удаление успешное
        print("Пользователь 'Alice' удален.")
    except UserNotFoundError as e:
        print(e)

    # Попробуем найти пользователей
    try:
        user_manager.find_user("Bob")  # Найдем Bob
        print("Пользователь 'Bob' найден.")
    except UserNotFoundError as e:
        print(e)

    try:
        user_manager.find_user("Charlie")  # Пользователь не существует
    except UserNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()