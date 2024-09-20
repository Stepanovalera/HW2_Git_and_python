

def  get_numbers():
    exp = int(input("Введите выражение: "))
    return exp

def calculate(a: float, b: float, operator: str):
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

def main():
    # Получение чисел
    exp = get_numbers()

    # Запрос операции
    operation = oper(exp)

    # Вычисление
    result = calculate(first, second, oper)

    # Вывод результат
    display(result)

if __name__ == "__main__":
    run()
