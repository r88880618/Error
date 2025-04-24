# Класс собственного исключения`NegativeNumberError`
"""
- Класс `NegativeNumberError` унаследован от базового класса `Exception`, что делает его полноценным 
объектом исключения.
- Конструктор (`__init__`) принимает два параметра: само число и необязательную строку описания ошибки. 
Сообщение формируется динамически с указанием конкретного передаваемого числа.
- Метод `__str__` переопределён для вывода сообщения об ошибке.
- Функция `check_positive_number` проверяет, положительно ли число. Если число отрицательно, функцмя 
выбрасывает собственное исключение `NegativeNumberError`.
"""

class NegativeNumberError(Exception):
    def __init__(self, number, message="Отрицательные числа запрещены"):
        self.number = number
        self.message = f"{message}: передано число {number}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return True


# Тестируем функцию с отрицательным числом
try:
    check_positive_number(-5)
except NegativeNumberError as ne:
    print(ne)

# Тестируем функцию с положительным числом
result = check_positive_number(10)
print(result)