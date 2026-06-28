"""
Расширенный калькулятор с математическими функциями.
Поддерживает:
1. Базовые операции: +, -, *, /
2. Возведение в степень: ** или ^
3. Квадратный корень: sqrt(число) или vчисло (используем v вместо корня)
4. Логарифм: log(число) - натуральный, log10(число) - десятичный
5. Модуль числа: abs(число)
6. Синус, косинус: sin(число), cos(число) (угол в градусах)
7. Факториал: fact(число) или число!
8. История вычислений (последние 5 операций)
"""

import math

# Глобальный список для хранения истории
history = []

def add_to_history(expression, result):
    """Добавляет запись в историю, сохраняя только последние 5."""
    history.append(f"{expression} = {result}")
    if len(history) > 5:
        history.pop(0)

def show_history():
    """Выводит сохраненную историю."""
    if not history:
        print("\n[История пуста]")
    else:
        print("\n--- Последние 5 вычислений ---")
        for item in history:
            print(f"  {item}")

def calculate_unary(operation, num):
    """
    Выполняет унарные операции (с одним числом):
    sqrt, log, log10, abs, sin, cos, fact
    """
    if operation == 'sqrt' or operation == 'v':
        if num < 0:
            return "Ошибка: нельзя извлечь корень из отрицательного числа!"
        return round(math.sqrt(num), 6)
    
    elif operation == 'log':
        if num <= 0:
            return "Ошибка: логарифм определён только для положительных чисел!"
        return round(math.log(num), 6)
    
    elif operation == 'log10':
        if num <= 0:
            return "Ошибка: логарифм определён только для положительных чисел!"
        return round(math.log10(num), 6)
    
    elif operation == 'abs':
        return abs(num)
    
    elif operation == 'sin':
        return round(math.sin(math.radians(num)), 6)
    
    elif operation == 'cos':
        return round(math.cos(math.radians(num)), 6)
    
    elif operation == 'fact' or operation == '!':
        if num < 0 or not num.is_integer():
            return "Ошибка: факториал определён только для целых неотрицательных чисел!"
        return math.factorial(int(num))
    
    else:
        return "Ошибка: неизвестная операция!"

def calculate_binary(num1, num2, operation):
    """
    Выполняет бинарные операции (с двумя числами):
    +, -, *, /, ** (степень)
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль!"
        return num1 / num2
    elif operation == '**' or operation == '^':
        return num1 ** num2
    else:
        return "Ошибка: неизвестная операция!"

def parse_input(user_input):
    """
    Разбирает ввод пользователя.
    Возвращает: (тип_операции, данные) или None при ошибке.
    """
    user_input = user_input.strip()
    
    # Проверка на команды
    if user_input.lower() == 'exit':
        return ('exit', None)
    elif user_input.lower() == 'history':
        return ('history', None)
    
    # Проверка на унарные операции (функции с одним числом)
    unary_ops = ['sqrt', 'log', 'log10', 'abs', 'sin', 'cos', 'fact', 'v']
    
    for op in unary_ops:
        if user_input.startswith(op + '(') and user_input.endswith(')'):
            try:
                num_str = user_input[len(op)+1:-1]
                num = float(num_str)
                return ('unary', (op, num))
            except ValueError:
                print("Ошибка: введите корректное число в {}(...)".format(op))
                return None
    
    # Проверка на факториал с восклицательным знаком (5!)
    if user_input.endswith('!'):
        try:
            num_str = user_input[:-1]
            num = float(num_str)
            return ('unary', ('!', num))
        except ValueError:
            print("Ошибка: введите корректное число перед !")
            return None
    
    # Проверка на бинарные операции (два числа)
    parts = user_input.split()
    
    if len(parts) == 3:
        try:
            num1 = float(parts[0])
            num2 = float(parts[2])
            op = parts[1]
            return ('binary', (num1, num2, op))
        except ValueError:
            print("Ошибка: введите корректные числа!")
            return None
    
    # Если не получилось, пробуем найти оператор в строке
    binary_ops = ['+', '-', '*', '/', '**', '^']
    for op in binary_ops:
        if op in user_input and not user_input.startswith(op):
            parts = user_input.split(op)
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    return ('binary', (num1, num2, op))
                except ValueError:
                    continue
    
    print("Ошибка: неверный формат ввода!")
    print("Примеры: 5 + 3, sqrt(25), log(100), 5!, 2**10")
    return None

def main():
    print("\n" + "="*50)
    print("РАСШИРЕННЫЙ КАЛЬКУЛЯТОР")
    print("="*50)
    print("\nДоступные операции:")
    print("  Базовые:    5 + 3, 10 - 4, 7 * 8, 15 / 3")
    print("  Степень:    2 ** 10  или  2^10")
    print("  Корень:     sqrt(25)  или  v25")
    print("  Логарифм:   log(100) - натуральный")
    print("  Логарифм:   log10(100) - десятичный")
    print("  Модуль:     abs(-5)")
    print("  Тригоном.:  sin(30), cos(60) (углы в градусах)")
    print("  Факториал:  fact(5)  или  5!")
    print("\nКоманды: 'history' - показать историю, 'exit' - выход")
    print("="*50 + "\n")
    
    while True:
        user_input = input("Введите выражение: ").strip()
        
        parsed = parse_input(user_input)
        if parsed is None:
            continue
        
        cmd_type, data = parsed
        
        if cmd_type == 'exit':
            print("\nДо свидания! Спасибо за использование калькулятора.")
            break
        elif cmd_type == 'history':
            show_history()
            continue
        elif cmd_type == 'unary':
            op, num = data
            result = calculate_unary(op, num)
            print("Результат: {}".format(result))
            
            if isinstance(result, (int, float)):
                add_to_history("{}({})".format(op, num), result)
        
        elif cmd_type == 'binary':
            num1, num2, op = data
            result = calculate_binary(num1, num2, op)
            print("Результат: {}".format(result))
            
            if isinstance(result, (int, float)):
                add_to_history("{} {} {}".format(num1, op, num2), result)

if __name__ == "__main__":
    main()
