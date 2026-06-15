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

    left, operator, right = problem

    try:
        left = float(left)
        right = float(right)
    except ValueError:
        raise ValueError("Invalid input. Try using numbers.")

    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Invalid operator. Use +, -, *, /")

    return left, operator, right

def calculate(left, operator, right):
    if operator == "+":
        return add(left, right)
    elif operator == "-":
        return subtract(left, right)
    elif operator == "*":
        return multiply(left, right)
    elif operator == "/":
        return divide(left, right)

def main():
    print("Basic CLI Calculator")
    print("Supported format; 5 + 2, 8 / 4, etc.")
    print("Supported operators: +, -, *, /")
    print("To exit the calculator type 'quit'")

    while True:
        user_input = input("> ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        try:
            left, operator, right = parse_input(user_input)
            result = calculate(left, operator, right)
            print("Result:", result)
        except ValueError as error:
            print("Error:", error)
        except ZeroDivisionError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()