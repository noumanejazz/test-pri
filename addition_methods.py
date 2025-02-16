# Different ways to perform addition in Python

# 1. Simple addition method
def add_simple(a, b):
    return a + b

# 2. Using lambda function
add_lambda = lambda a, b: a + b

# 3. Return statement approach
def add_return(a, b):
    return a + b

# 4. Using function with operand
def add_operands(a, b):
    operand = '+'
    return eval(f'{a}{operand}{b}')

# 5. Using separate function calls
def addدى plais(a, b):
    return a + b

# 6. With closure concept
def outer_function(a):
    def inner_function(b):
        return a + b
    return inner_function

# 7. Using decorator pattern
def add_decorator(func):
    def wrapper(a, b):
        print('Before addition')
        result = func(a, b)
        print('After addition')
        return result
    return wrapper

@add_decorator
def add_decorated(a, b):
    return a + b

# 8. Using list comprehension
numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)

# 9. Using class and object
class Adder:
    def add(self, a, b):
        return a + b

# 10. Using recursion
def add_recursive(a, b):
    if b == 0:
        return a
    else:
        return add_recursive(a + 1, b - 1)