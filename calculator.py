

def  get_numbers():
    exp = int(input("Введите выражение: "))
    return exp

# ОБЪЯВЛЯЮ ФУНКЦИЮ calc()
def calc(a: float, b: float, operator: str):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Ошибка: Деление на ноль!"
    else:
        result = "Я умею только складывать, вычитать, умножать и делить"
    return result

# РАСЧЁТ И ВЫВОД ОТВЕТА
result = calc(a, b, operator)

# Вывод результата
print(f"Результат: {result}")

