def calculate_expression(a, b):
    part1 = a + 4 * b
    part2 = a - 3 * b
    result = part1 * part2 + a ** 2
    return result

a_val = 2
b_val = 3
res = calculate_expression(a_val, b_val)
print(f"Результат выражения: {res}")
print("\n")