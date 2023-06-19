def ReadInt(args,long):
    
    entrence = input(f"input {args}, len = {long}: ")
    
    while (len(entrence) != long ):
        entrence = input(f"invalid data, len =/= {long}, again: ")
        
    return entrence
    

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

def task_2():
    number = int(ReadInt("three-digit number:", 3))
    sum = 0
    
    while (number >= 1):
        sum += number % 10
        number = number // 10
        
    return sum



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def task_4():
    
    s = int(input("multiply 6: "))
    while(s % 6 != 0):
        s = int(input(f"{s} not a multiple of 6, again: "))
    
    x = s // 6
    
    return f"Петя {x}, Катя {4 * x}, Сережа {x}"
    



# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no


def task_6():
    bilet = ReadInt("ticket, 6 nymbers: ", 6)
    bList = []
    
    for char in bilet:
        bList.append(int(char))

    if sum(bList[:len(bList)//2]) == sum(bList[3:len(bList)]):
        return "yes, lucky"
    else:
        return "unlucky"




# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


def task_8():
    firstSide = int(input("1 side: "))
    secondSide = int(input("2 side: "))
    chocoSlice = int(input("need: "))
    
    if (chocoSlice % firstSide == 0 or chocoSlice % secondSide == 0) and chocoSlice <= (firstSide * secondSide):
        return True
    else:
        return False


