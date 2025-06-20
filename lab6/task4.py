sequence = [-5, -3, -1, 2, 4, 6, -2, 0, 8]

first_positive = next((x for x in sequence if x > 0), None)
print(f"Первый положительный элемент: {first_positive}")

last_negative = next((x for x in reversed(sequence) if x < 0), None)
print(f"Последний отрицательный элемент: {last_negative}")