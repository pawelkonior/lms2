from decimal import Decimal

import pytest


def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Something is no yes')
    return a / b


def test_should_divide_correctly():
    assert divide(4, 2) == 2


def test_divide_with_wrong_result():
    assert divide(10, 5) != 3


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as ctx_info:
        divide(10, 0)


def test_division_using_string_raise_exception():
    with pytest.raises(TypeError) as ctx_info:
        divide(10, '2')


def test_division_using_decimal_raise_exception():
    with pytest.raises(TypeError) as ctx_info:
        divide(Decimal(10), 3)
