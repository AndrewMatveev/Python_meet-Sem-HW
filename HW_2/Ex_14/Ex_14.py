# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


import math

n = int(input('Задай число: '))

temp = n
count = 0

while n > 1:
    n = n / 2
    count += 1
# print(count)

for i in range(1, count + 1):
    temp2 = int(math.pow(2, i))
    if temp2 <= temp:
        print(temp2)