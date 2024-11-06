print("Меню\nВыберите нужную вам фигуру(а,б,в,г...)")
fig = str(input("Фигура "))
size = int(input("Размер фигуры = "))
if fig == "а" or fig == "А":
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or j > i:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "б" or fig == "Б":
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or j < i:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "в" or fig == "В":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or i < j and i < size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "г" or fig == "Г":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or i > j and i > size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "д" or fig == "Д":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or i > j and i > size - 1 - j or i < j and i < size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "е" or fig == "Е":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or i > j and i < size - 1 - j or i < j and i > size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "ж" or fig == "Ж":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or j < i and j < size - 1 - i:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "з" or fig == "З":
    for i in range(size):
        for j in range(size):
            if i==0 or i==size-1 or j==0 or j==size-1 or j > i and j > size - 1 - i:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "и" or fig == "И":
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or (i > j and i < size - 1 - j)  or i < j and i < size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()
if fig == "к" or fig == "К":
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1 or (i < j and i > size - 1 - j)  or i > j and i > size - 1 - j:
                print("*", end="")
            else:
                print(" ", end='')
        print()

