# функция, которая спрашивает, хочет ли человек продолжить расчет
def end():
    while True:
        x = input('Вы хотите совершить еще один расчет?\nОтвет: да/нет ').lower()
        if x == 'да':
            return False
            break
        elif x == 'нет':
            return True
            break
        else: 
            print('Неподходящий ответ')

# функция возвращает F или T, соотвественно, в цикле ее можно указать в виде if end():
# if end():
#     print('Конец программы')
# else:
#     print('Расчет дальше')

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

def display(result):
    print("Результат: ", result)

def main():
     while True:
    # Получение чисел
        exp = get_numbers()

    # Запрос операции
        operation = oper(exp)

    # Вычисление
        result = calculate(first, second, oper)

    # Вывод результат
        display(result)

    #Реализует функцию end()
        if end():
            print('Конец программы')
            break

if __name__ == "__main__":
    main()
