# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


def task16():
    
    a = int(input("размер, задача 16: "))
    array = list()
    
    i = 0
    while i < a:
        array.append(int(input(f"добавить на позицию {i+1}: ")))
        i +=1
    
    b = int(input("найти кол-во повторений числа: "))
    count = 0
    
    for j in array:
        if j == b:
            count += 1
    
    if count == 0:
        return f"{b} nonexist"
    
    print(array)
    return count
    
    
# print(task16())


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


def task18():
    a = int(input("размер, задача 18: "))
    array = list()
    
    i = 0
    while i < a:
        array.append(int(input(f"добавить на позицию {i+1}: ")))
        i += 1
    
    b = int(input("найти ближайшее: "))

    minIndex = 0
    currentABS = abs(array[minIndex] - b)
    
    for j in range(1, len(array)):
        nextABS = abs(array[j] - b) 
        if nextABS <= currentABS: 
            minIndex = j
        currentABS = nextABS
        
    print(array)
    print(f"{minIndex}->{array[minIndex]}")
    
    return array[minIndex]
            
print(task18())
