def calculate(arr):
    sum_positive = 0
    for num in arr:
        if num > 0:
            sum_positive += num

    min_index = 0
    max_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i

    start = min_index if min_index < max_index else max_index
    end = max_index if max_index > min_index else min_index

    product = 1
    for i in range(start + 1, end):
        product = product * arr[i]

    return sum_positive, product

array = [3, -1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sum_pos, prod = calculate(array)
print(f"Сумма положительных: {sum_pos}, Произведение между min и max: {prod}")
print("\n")