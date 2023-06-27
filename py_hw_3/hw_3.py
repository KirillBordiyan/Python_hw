# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


def task16():
    
    a = int(input("размер: "))
    array = list()
    
    i = 0
    while i < a:
        array.append(int(input(f"добавить на позицию {i+1}: ")))
        i +=1
    
    b = int(input("найти: "))
    count = 0
    
    for j in array:
        if j == b:
            count += 1
    
    if count == 0:
        return f" {b} nonexist"
    
    print(array)
    return count
    
    
print(task16())