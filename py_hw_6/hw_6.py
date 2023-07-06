import random
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def task30():
    
    firstElemProgr = int(input("task 30 первый элемент: "))
    scale = int(input("task 30 разность между элементами: "))
    lenghtOfProgr = int(input("task 30 найти элемент: "))
    arifm = [firstElemProgr]
    
    arifm = [firstElemProgr+((i-1)*scale) for i in range(1,lenghtOfProgr+1)]
    
    return arifm
    
print(task30())



# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def task32():
    start = int(input("task 32 От: "))
    end = int(input("task 32 До: "))
    arrayOFNumbers = [random.randint(-100, 101) for _ in range(15)]
    result = [i for i in arrayOFNumbers if start<i<end]
    
    print(arrayOFNumbers)
    print(result)
    
task32()    
    