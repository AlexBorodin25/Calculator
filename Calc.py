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

    left, operator, right = problem

    if len(problem) != 3:
        raise ValueError("Invalid input. Try (5 + 2) format.")

    try:
        left = float(left)
        right = float(right)
    except ValueError:
        raise ValueError("Invalid input. Try using numbers.")

    if operator not in ["+", "-", "x", "÷"]:
        raise ValueError("Invalid operator. Use +, -, x, ÷")

    return left, operator, right

def calculate(left, operator, right):
    if operator == "+":
        return add(left, right)
    elif operator == "-":
        return subtract(left, right)
    elif operator == "x":
        return multiply(left, right)
    elif operator == "÷":
        return divide(left, right)

def main():
    user_input = input("> ")

    if user_input.lower() == "quit"
        print("Goodbye!")
        break
    try:
        left, operator, right = parse_input(user_input)
        result = calculate(left, operator, right)
        print("Result:", result)
    except ValueError:
        print("Error:", error)
    except ZeroDivisionError:
        print("Error:", error)

if __name__ == "__main__":
    main()