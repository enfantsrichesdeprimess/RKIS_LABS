import random

arr = [0] * 15
for i in range(15):
    arr[i] = random.randint(1, 100)

print("Array elements:")
for element in arr:
    print(element, end=' ')
print("\n")