def square(x: int | float) -> int | float:
    """square calculate and return"""
    return x ** 2

def pow(x: int | float) -> int | float:
    """power calculate and return"""
    return x ** x

def outer(x: int | float, function) -> object:
    """init count and return function that apply argument function"""
    count = x
    def inner() -> float:
        """use extern count value.
        apply function, update count value"""
        nonlocal count
        count = function(count)
        return count
    return inner
