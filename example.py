from decimal import Decimal


class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Something is no yes')
    return a / b


# test, czy dzieli poprawnie
if divide(4, 2) == 2:
    print(f'{Colors.OKGREEN}.{Colors.ENDC}')
else:
    print(f'{Colors.FAIL}F{Colors.ENDC}')

# test, czy wynik jest niepoprawny
if divide(10, 5) != 3:
    print(f'{Colors.OKGREEN}.{Colors.ENDC}')
else:
    print(f'{Colors.FAIL}F{Colors.ENDC}')

# test, czy dzielenie przez 0 daje błąd
try:
    divide(10, 0)
    print(f'{Colors.FAIL}F{Colors.ENDC}')
except ZeroDivisionError as err:
    print(f'{Colors.OKGREEN}.{Colors.ENDC}')

# test, czy funkcja obsługuje nie int lub nie float
try:
    divide(10, '2')
    print(f'{Colors.FAIL}F{Colors.ENDC}')
except TypeError as err:
    print(f'{Colors.OKGREEN}.{Colors.ENDC}')

# test, czy funkcja nie obsługuje Decimal
try:
    divide(Decimal(10), 3)
    print(f'{Colors.FAIL}F{Colors.ENDC}')
except TypeError as err:
    print(f'{Colors.OKGREEN}.{Colors.ENDC}')
