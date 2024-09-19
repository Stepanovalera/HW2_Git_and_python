
from calc import calculate
from result import display

def  get_numbers():
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    return first, second

def run():
    # Получение чисел
    first, second = get_numbers()

    # Запрос операции
    operation = input("Введите операцию (+, -, *, /): ")

    # Вычисление
    result = calculate(first, second, operation)

    # Вывод результат
    display(result)

if __name__ == "__main__":
    run()