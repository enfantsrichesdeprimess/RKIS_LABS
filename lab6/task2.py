class User:
    def __init__(self, login, password):
        self.Login = login
        self.Password = password

users = [
    User("admin", "12345"),
    User("user1", "qwerty"),
    User("user2", "password"),
    User("guest", "guest"),
    User("test", "test123")
]

target_login = "user2"
target_password = "password"

for user in users:
    if user.Login == target_login and user.Password == target_password:
        print(f"Найден пользователь: Логин - {user.Login}, Пароль - {user.Password}")
        break
else:
    print("Пользователь не найден")