def count_elements_start_end_with_C(C, A):
    count = 0
    for element in A:
        if len(element) > 1 and element.startswith(C) and element.endswith(C):
            count += 1
    return count

C = 'a'
A = ['apple', 'banana', 'aba', 'aa', 'acacia', 'a']

result = count_elements_start_end_with_C(C, A)
print(f"Количество элементов: {result}")