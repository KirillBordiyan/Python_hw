# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def task26(a,b):  
    if b == 0:
        return 1
    if b < 0:
        return 1/a*task26(a, b+1)
    return a*task26(a, b-1)
    
print(task26(int(input("task 26 A: ")), int(input("task 26 B: "))))




# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4


def task28(a,b):
    if a < 0:
        a = int(input("A again: "))
    if b < 0:
        b = int(input("B again: "))
    if a < b:
        temp = a
        a = b
        b = temp
    if b == 0:
        return a
    return task28(a+1,b-1)


print(task28((int(input("task 28 A: "))), int(input("task 28 B: "))))
