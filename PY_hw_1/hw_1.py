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

print(task_2())
