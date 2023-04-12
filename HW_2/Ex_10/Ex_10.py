# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

import random 
n = int(input("Insert volume of coins: "))

barkhatnye = tagi = 0

for i in range(n):
    kefteme = random.randint(0, 1)
    if kefteme == 1: print("Орёл")
    else: print("Решка")
    tagi += kefteme
barkhatnye = n - tagi

if tagi < barkhatnye: print(f"Minimal count is {tagi}")
else: print(f"Minimal count is {barkhatnye}")