arr2 = [0] * 15
total = 0
for i in range(14):
    try:
        arr2[i] = int(input(f"Enter element {i + 1}: "))
        total += arr2[i]
    except:
        print("Please enter numbers only!")
        exit()

arr2[14] = total

print("Array elements:")
for x in arr2:
    print(x, end=' ')
print("\n")