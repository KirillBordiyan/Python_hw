# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def task30():
    
    firstElemProgr = int(input("первый элемент: "))
    scale = int(input("разность между элементами: "))
    lenghtOfProgr = int(input("найти элемент: "))
    arifm = [firstElemProgr]
    
    arifm = [firstElemProgr+((i-1)*scale) for i in range(1,lenghtOfProgr+1)]
    
    return arifm
    
print(task30())
