# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

start_numb = int(input("Ввод начала диапазона: "))

end_numb = int(input("Ввод окончания диапазона: "))

n = int(input("Ввод размера массива: "))

list_1 = [random.randint (-10, 10) for i in range(n)]
list_2 = []

print(list_1)

for i in range(n):
    if list_1[i] >= start_numb and list_1[i] <= end_numb:
        list_2.append(i)

print(list_2)