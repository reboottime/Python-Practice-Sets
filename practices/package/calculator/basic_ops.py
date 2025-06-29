import numbers

 # No type specified here for num1 & num2
def add(num1, num2)  -> numbers.Number:
    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        return num1 + num2
    else:
        raise TypeError(f"Expected a input params as numbers. num1: ${num1}, num2:${num2}")

def substract(num1, num2) -> numbers.Number:
    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        return num1 - num2
    else:
        raise TypeError(f"Expected a input params as numbers. num1: ${num1}, num2:${num2}")

"""
# for concise comment
from typing import TypeVar
from numbers import Number

T = TypeVar('T', bound=Number)

def add(a: T, b: T) -> T:
    return a + b
    
"""