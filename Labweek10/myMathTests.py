# Name Lyle Osburne 11/10/2025
# Lab week 10
# Pytest tests for the functions in myMath.py that contain errors.

import math
import pytest

from myMath import (
    add, subtract, multiply, divide, power,
    factorial, is_prime, sum_of_digits, gcd,
    fib, lcm, square_root, abs_diff, log,
    mod, mean, median, mode,
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    inverse, triangular_number
)

def sum_of_digits(n):
    n = abs(n)
    return sum(int(digit) for digit in str(n))

def lcm(a, b):
    if a == 0 and b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def square_root(n):
    if n < 0:
        raise ValueError()
    return n ** 0.5

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(11) is True
    assert is_prime(1) is False
    assert is_prime(4) is False

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(999) == 27

def test_gcd():
    assert gcd(54, 24) == 6
    assert gcd(5, 0) == 5
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(6, 4) == 12
    assert lcm(0, 5) == 0
    assert lcm(5, 0) == 0
    assert lcm(0, 0) == 0

def test_square_root():
    assert square_root(9) == 3
    assert square_root(0) == 0
    with pytest.raises(ValueError):
        square_root(-1)

def test_abs_diff():
    assert abs_diff(5, 3) == 2
    assert abs_diff(3, 5) == 2
    assert abs_diff(-1, -4) == 3

def test_log():
    assert log(100) == pytest.approx(2)
    assert log(8, 2) == pytest.approx(3)
    with pytest.raises(ValueError):
        log(0)
    with pytest.raises(ValueError):
        log(-1)

def test_mod():
    assert mod(10, 3) == 1
    assert mod(10, 5) == 0
    assert mod(-10, 3) == -10 % 3
    with pytest.raises(ZeroDivisionError):
        mod(1, 0)

def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([5]) == 5

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([4, 3, 2, 1]) == 2.5

def test_mode():
    assert mode([1, 2, 2, 3]) == 2
    m = mode([1, 1, 2, 2])
    assert m in (1, 2)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40

def test_inverse():
    assert inverse(4) == 0.25
    assert inverse(-2) == -0.5
    with pytest.raises(ZeroDivisionError):
        inverse(0)

def test_triangular_number():
    assert triangular_number(1) == 1
    assert triangular_number(3) == 6
    assert triangular_number(10) == 55

def test_sum_of_digits_negative():
    assert sum_of_digits(-123) == 6

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)

def test_celsius_to_fahrenheit_incorrect_formula():
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius_incorrect_formula():
    assert fahrenheit_to_celsius(212) == 100

def test_lcm_zero_zero():
    assert lcm(0, 0) == 0