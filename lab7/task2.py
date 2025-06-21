import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10,10))

positive_numbers = [x for x in numbers if x > 0]
print(numbers)
print(f"Положительные числа: {positive_numbers}")