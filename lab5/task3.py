import random


def generate_sorted_even(size):
    arr = []
    while len(arr) < size:
        num = random.randint(1, 100)
        if num % 2 == 0:
            arr.append(num)
    arr.sort()
    return arr


sorted_even = generate_sorted_even(10)
print("Случайные четные числа:", sorted_even)
print("\n")