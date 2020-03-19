def add(x, y):
    """add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """multiply function"""
    return x * y


def divide(x, y):
    """divide function"""
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y


def divideUsingCheck(numerator, denominator):
    """divide function using an if check to avoid divide by zero"""
    return numerator / denominator if denominator else 0
