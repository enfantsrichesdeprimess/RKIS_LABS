class MathOperations:
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4


def calculate(a, b, operation):
    if operation == MathOperations.PLUS:
        result = a + b
    elif operation == MathOperations.MINUS:
        result = a - b
    elif operation == MathOperations.MULTIPLY:
        result = a * b
    elif operation == MathOperations.DIVIDE:
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
    else:
        result = "Invalid operation"

    return (a, b, operation, result)

first_num = 10
second_num = 5
op = MathOperations.PLUS
result_tuple = calculate(first_num, second_num, op)
print(f"Calculation: {result_tuple[0]} {op} {result_tuple[1]} = {result_tuple[3]}\n")