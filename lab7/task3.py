import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10,50))

two_digit_numbers = sorted([x for x in numbers if 10 <= x <= 99])
print(numbers)
print(f"Отсортированные двузначные числа: {two_digit_numbers}")