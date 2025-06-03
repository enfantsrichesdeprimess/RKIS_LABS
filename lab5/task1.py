def sum_between(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


n = int(input("Введите число N: "))
result = sum_between(n)
print(f"Сумма чисел от 1 до {n}: {result}")
print("\n")
