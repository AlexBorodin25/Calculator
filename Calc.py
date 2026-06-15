def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def parse_input(user_input):
    problem = user_input.strip().split()

    if len(problem) != 3:
        raise ValueError("Invalid input. Try (5 + 2) format.")