def invert_signs(arr):
    new_arr = []
    for num in arr:
        new_arr.append(-num)
    return new_arr

original = [1, -5, 0, 3, -4]
inverted = invert_signs(original)
print("Оригинал:", original)
print("Инвертированный:", inverted)
print("\n")