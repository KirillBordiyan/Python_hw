import random
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


def task22():
    n = int(input("task 22 long 1: "))
    m = int(input("task 22 long 2: "))
    
    unionAll = list(set([int(input()) for _ in range(n)]).intersection(set([int(input()) for _ in range(m)])))
    
    print(unionAll)
    
task22()





# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.



def task24():
    bush = [random.randint(1,101) for _ in range(int(input("task 24 bush length: ")))]
    print(bush)

    sumInner = 0
    sumMax = 0
    position = 0
    
    for i in range(len(bush)):
        if i == 0:
            sumInner = bush[len(bush)-1] + bush[0] + bush[1]
        elif i == len(bush)-1:
            sumInner = bush[len(bush)-2] + bush[len(bush)-1] + bush[0]
            position = i
        else:
            sumInner =  bush[i-1] + bush[i] + bush[i+1]
        if sumInner > sumMax:
            sumMax = sumInner
            position = i        
    
    print(f"{sumMax} if start {position}")
        
    
task24()
