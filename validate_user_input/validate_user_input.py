# Фуекция validate_user_input(data), которая принимает словарь с данными пользователя
"""
Проверку корректности введённых данных проводим с использованием функции isinstance()
- Проверка типа данных: Сначала функция проверяет, является ли входные данные словарем. 
Если нет, она вызывает TypeError с соответствующим сообщением.
- Проверка ключа name: Если ключ 'name' отсутствует в словаре или его значение не является 
строкой, поднимается ValueError.
- Проверка ключа age: Если ключ 'age' отсутствует или его значение не является положительным 
числом (проверка на int или float и проверка на большее 0), также поднимается ValueError.
- В конструкции raise...from убираем from, чтобы видеть полный стек исключений
"""

def validate_user_input(data):
    # Проверка, что data является словарем
    if not isinstance(data, dict):
        raise TypeError(f"Ожидался словарь, получен {type(data).__name__}.")
    
    # Проверка ключа name
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError("Ключ 'name' должен присутствовать и быть строкой.")
    
    # Проверка ключа age
    if 'age' not in data or not (isinstance(data['age'], (int, float)) and data['age'] > 0):
        raise ValueError("Ключ 'age' должен присутствовать и быть положительным числом.")

# Тестирование функции validate_user_input()
try:
    # Корректные данные
    validate_user_input({"name": "Alice", "age": 30})
    print("Данные валидны.")
except Exception as e:
    print(f"Ошибка: {e}")

try:
    # Отсутствует ключ 'name'
    validate_user_input({"age": 30})
except Exception as e:
    print(f"Ошибка: {e}")

try:
    # Некорректное значение для 'age'
    validate_user_input({"name": "Alice", "age": "тридцать"})
except Exception as e:
    print(f"Ошибка: {e}")

try:
    # Некорректный тип входных данных
    validate_user_input("это не словарь")
except Exception as e:
    print(f"Ошибка: {e}")

try:
    # Отрицательное значение для 'age'
    validate_user_input({"name": "Alice", "age": -5})
except Exception as e:
    print(f"Ошибка: {e}")

