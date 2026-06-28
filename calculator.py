"""
Расширенный калькулятор с математическими функциями.

Консольный калькулятор с поддержкой базовых операций,
логарифмов, корней, тригонометрии, факториала и истории вычислений.

Автор: Ваше Имя
GitHub: https://github.com/ваш-username/calculator
"""

import math


class Calculator:
    """Основной класс калькулятора с историей и математическими операциями."""
    
    def __init__(self):
        """Инициализация калькулятора с пустой историей."""
        self.history = []
        self.max_history = 5
    
    def add_to_history(self, expression, result):
        """
        Добавляет вычисление в историю (хранит только последние 5 записей).
        
        Аргументы:
            expression (str): Математическое выражение
            result (float/int): Результат вычисления
        """
        self.history.append(f"{expression} = {result}")
        if len(self.history) > self.max_history:
            self.history.pop(0)
    
    def get_history(self):
        """
        Возвращает историю вычислений.
        
        Возвращает:
            list: Список исторических записей
        """
        return self.history
    
    def clear_history(self):
        """Очищает всю историю вычислений."""
        self.history.clear()
    
    def calculate_unary(self, operation, num):
        """
        Выполняет унарные операции (с одним числом).
        
        Поддерживаемые операции:
            sqrt/v  - Квадратный корень
            log     - Натуральный логарифм
            log10   - Десятичный логарифм
            abs     - Модуль числа
            sin     - Синус (в градусах)
            cos     - Косинус (в градусах)
            fact/!  - Факториал
        
        Аргументы:
            operation (str): Название операции
            num (float): Входное число
        
        Возвращает:
            float или str: Результат или сообщение об ошибке
        """
        if operation == 'sqrt' or operation == 'v':
            if num < 0:
                return "Ошибка: нельзя извлечь корень из отрицательного числа"
            return round(math.sqrt(num), 6)
        
        elif operation == 'log':
            if num <= 0:
                return "Ошибка: логарифм определён только для положительных чисел"
            return round(math.log(num), 6)
        
        elif operation == 'log10':
            if num <= 0:
                return "Ошибка: логарифм определён только для положительных чисел"
            return round(math.log10(num), 6)
        
        elif operation == 'abs':
            return abs(num)
        
        elif operation == 'sin':
            return round(math.sin(math.radians(num)), 6)
        
        elif operation == 'cos':
            return round(math.cos(math.radians(num)), 6)
        
        elif operation == 'fact' or operation == '!':
            if num < 0 or not num.is_integer():
                return "Ошибка: факториал определён только для целых неотрицательных чисел"
            return math.factorial(int(num))
        
        else:
            return "Ошибка: неизвестная операция"
    
    def calculate_binary(self, num1, num2, operation):
        """
        Выполняет бинарные операции (с двумя числами).
        
        Поддерживаемые операции:
            +   - Сложение
            -   - Вычитание
            *   - Умножение
            /   - Деление
            **/^ - Возведение в степень
        
        Аргументы:
            num1 (float): Первое число
            num2 (float): Второе число
            operation (str): Оператор
        
        Возвращает:
            float или str: Результат или сообщение об ошибке
        """
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        elif operation == '**' or operation == '^':
            return num1 ** num2
        else:
            return "Ошибка: неизвестная операция"
    
    def parse_input(self, user_input):
        """
        Разбирает ввод пользователя на операции.
        
        Аргументы:
            user_input (str): Входная строка
        
        Возвращает:
            tuple: (тип_операции, данные) или None если неверный формат
        """
        user_input = user_input.strip()
        
        # Проверка на команды
        if user_input.lower() == 'exit':
            return ('exit', None)
        elif user_input.lower() == 'history':
            return ('history', None)
        elif user_input.lower() == 'clear':
            return ('clear', None)
        
        # Проверка на унарные операции: func(число)
        unary_ops = ['sqrt', 'log', 'log10', 'abs', 'sin', 'cos', 'fact', 'v']
        
        for op in unary_ops:
            if user_input.startswith(op + '(') and user_input.endswith(')'):
                try:
                    num_str = user_input[len(op)+1:-1]
                    num = float(num_str)
                    return ('unary', (op, num))
                except ValueError:
                    return None
        
        # Проверка на факториал с восклицательным знаком: 5!
        if user_input.endswith('!'):
            try:
                num_str = user_input[:-1]
                num = float(num_str)
                return ('unary', ('!', num))
            except ValueError:
                return None
        
        # Проверка на бинарные операции с пробелами: 5 + 3
        parts = user_input.split()
        if len(parts) == 3:
            try:
                num1 = float(parts[0])
                num2 = float(parts[2])
                op = parts[1]
                return ('binary', (num1, num2, op))
            except ValueError:
                return None
        
        # Проверка на бинарные операции без пробелов: 5+3
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
        
        return None
    
    def run(self):
        """Запускает интерактивный режим калькулятора."""
        print("\n" + "="*50)
        print("РАСШИРЕННЫЙ КАЛЬКУЛЯТОР")
        print("="*50)
        print("\nДоступные операции:")
        print("  Базовые:    5 + 3, 10 - 4, 7 * 8, 15 / 3")
        print("  Степень:    2 ** 10  или  2^10")
        print("  Корень:     sqrt(25)  или  v(25)")
        print("  Логарифм:   log(100) - натуральный")
        print("  Логарифм:   log10(100) - десятичный")
        print("  Модуль:     abs(-5)")
        print("  Тригоном.:  sin(30), cos(60) (углы в градусах)")
        print("  Факториал:  fact(5)  или  5!")
        print("\nКоманды:")
        print("  history  - Показать последние 5 вычислений")
        print("  clear    - Очистить историю")
        print("  exit     - Выйти из программы")
        print("="*50 + "\n")
        
        while True:
            user_input = input("Введите выражение: ").strip()
            
            if not user_input:
                continue
            
            parsed = self.parse_input(user_input)
            if parsed is None:
                print("Ошибка: неверный формат ввода")
                print("Примеры: 5 + 3, sqrt(25), log(100), 5!, 2**10")
                continue
            
            cmd_type, data = parsed
            
            if cmd_type == 'exit':
                print("\nДо свидания!")
                break
            elif cmd_type == 'history':
                if not self.history:
                    print("[История пуста]")
                else:
                    print("\n--- Последние 5 вычислений ---")
                    for item in self.history:
                        print(f"  {item}")
                continue
            elif cmd_type == 'clear':
                self.clear_history()
                print("[История очищена]")
                continue
            elif cmd_type == 'unary':
                op, num = data
                result = self.calculate_unary(op, num)
                print(f"Результат: {result}")
                
                if isinstance(result, (int, float)):
                    self.add_to_history(f"{op}({num})", result)
            
            elif cmd_type == 'binary':
                num1, num2, op = data
                result = self.calculate_binary(num1, num2, op)
                print(f"Результат: {result}")
                
                if isinstance(result, (int, float)):
                    self.add_to_history(f"{num1} {op} {num2}", result)


def main():
    """Точка входа в программу."""
    calc = Calculator()
    calc.run()


if __name__ == "__main__":
    main()
