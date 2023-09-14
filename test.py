from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления квадратного корня из заданного числа'


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Проверяет чтоб значение не было равно нулю."""
    if your_number <= 0:
        return 0
    num = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {num}')


print(message)
calc(25.5)