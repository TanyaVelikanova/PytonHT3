#Задача 1. Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.

import os
os.system('cls||clear')
spisok = [i for i in range(1, 20, 2)]
print(spisok)
sum=0
for i in range(len(spisok)):
    if i%2 != 0:
        sum+=spisok[i]
print(f'сумма элементов, стоящих на нечетных позициях = {sum}')

#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import os
os.system('cls||clear')
spisok = [i for i in range(1, 10, 1)]
print(f'список {spisok}')
len = len(spisok)
print(len)
i = 1
spisok_mult = []
if len%2 == 0:
    while i <= (len-i):
        multiply = spisok[i-1]*spisok[-i]
        spisok_mult.append(multiply)
        i = i+1
else:
    while i <= ((len+1)-i):
        multiply = spisok[i-1]*spisok[-i]
        spisok_mult.append(multiply)
        i = i+1    
print(f'список произведений {spisok_mult}')

#Задача 3. 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
#*Пример:*  - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)

import os
os.system('cls||clear')
spisok = [1.1, 1.2, 3.1, 5, 10.01]
spisok_str = []
spisok_dpart = []
spisok_str = list(map(str, spisok))
print(spisok_str)
for i in range(len(spisok_str)):
    element = spisok_str[i]
    ind_element = spisok_str[i].find('.')
    if ind_element == -1:
       continue
    dpart = '0.'
    for j in range((ind_element+1), len(element)):
        dpart = dpart + element[j]
    spisok_dpart.append(float(dpart))
print(spisok_dpart)
result = max(spisok_dpart) - min(spisok_dpart)
print(result)

# Задача 4. 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system('cls||clear')
number_ten = int(input('Введите число '))
ost = ''
while number_ten != 0:
    ost = str(number_ten%2) + ost
    number_ten=number_ten//2
print(ost)

