# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


def coins():
    
    coinList = [1, 0, 0, 0, 1, 1, 1, 1]
    re = 0 #0
    ge = 0 #1
    min = 0
    
    for i in coinList:
        if i == 0:
            re += 1
        else:
            ge += 1
    if re < ge:
        min = re
    else:
        min = ge
    
    return min

print(coins())
    