from math_functions import (
    add, subtract, multiply, divide, is_even, 
    max_of_two, factorial, is_prime
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(5, 0) is None

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True

def test_max_of_two():
    assert max_of_two(5, 3) == 5
    assert max_of_two(1, 10) == 10
    assert max_of_two(7, 7) == 7

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(-5) is None

def test_is_prime():
    """Тесты для функции is_prime"""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
    # Дополнительные тесты
    assert is_prime(11) is True
    assert is_prime(15) is False
    assert is_prime(97) is True