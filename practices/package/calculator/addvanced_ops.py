import numbers
from numbers import Number

# Type hints added for consistency
def multiply(num1: numbers.Number, num2: numbers.Number) -> numbers.Number:
    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        return num1 * num2
    else:
        raise TypeError(f"Expected input params as numbers. num1: {num1}, num2: {num2}")

def divide(a: Number, b: Number) -> Number:
    # Check zero FIRST - fail fast!
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    # Only do type checking if we passed the zero check
    if not (isinstance(a, Number) and isinstance(b, Number)):
        raise TypeError("Both arguments must be numbers")
    
    return a / b
