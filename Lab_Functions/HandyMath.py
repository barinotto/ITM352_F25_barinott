# HandyMath.py

def midpoint(a, b):
    """Return the value halfway between two numbers."""
    return (a + b) / 2

def squareroot(n):
    """Return the square root of a number."""
    return n ** 0.5

def describe_function(x, y, func):
    """
    Apply the given function to x and y, and return a descriptive string.
    """
    result = func(x, y)
    return f"The function {func.__name__} {x}, {y} = {result}"

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def max(a, b):
    """Custom max function."""
    return a if a > b else b

def min(a, b):
    """Custom min function."""
    return a if a < b else b
