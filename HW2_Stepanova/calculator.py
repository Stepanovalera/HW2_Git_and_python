

def  get_numbers():
    exp = int(input("Введите выражение: "))
    return exp

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
