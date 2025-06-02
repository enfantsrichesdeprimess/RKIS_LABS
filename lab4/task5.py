def risky_operations():
    try:
        a = 10
        b = 0
        c = a / b
        print(c)
    except:
        print("ошибка, на ноль далить нельзя")
    try:
        num = int("hello")
        print(num)
    except:
        print("Ошибка формата данных")
    try:
        arr = [1, 2, 3]
        print(arr[5])
    except:
        print("Индекс выходит за длинну массива")

risky_operations()