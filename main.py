def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def calculator():
    while True:
        print("\n===== Простой калькулятор =====")
        print("Доступные операции: +, -, *, /")

        try:
            a = float(input("Введите первое число: "))
            op = input("Выберите операцию (+, -, *, /): ")
            b = float(input("Введите второе число: "))

            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("Ошибка: неизвестная операция!")
                continue

            print("Результат:", result)

        except ValueError:
            print("Ошибка: некорректный ввод числа!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

       
        again = input("\nХотите выполнить еще одну операцию? (да/нет): ").strip().lower()
        if again != 'да':
            print("Выход из калькулятора. До свидания!")
            break

calculator()
