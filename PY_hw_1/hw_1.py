import math

def ReadInt(args,long):
    
    entrence = input(f"input {args}, len = {long}: ")
    
    while (len(entrence) != long ):
        entrence = input(f"invalid data, len =/= {long}, again: ")
        
    return int(entrence)
    

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


def task_2():
    number = ReadInt("number task 2", 3)
    sum = 0
    
    while (number >= 1):
        sum += number % 10
        number = number // 10
        
    return sum


# print(task_2())




# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def task_4():
    
    s = int(input("количество, кратное 6: "))
    while(s % 6 != 0):
        s = int(input(f"{s} не кратно 6, еще раз: "))
    
    x = s // 6
    
    return f"Петя {x}, Катя {4 * x}, Сережа {x}"
    

print(task_4())
