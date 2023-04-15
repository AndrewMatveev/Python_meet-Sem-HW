# Нужно создать рандомный массив A, который будет содержать определеннык кол-во цифр в любом порядке. Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если есть число Х, то оно и будет самым близким.

# _________________РЕШЕНИЕ__________________

import random

strt = int(input('Введите дипазон генерации.\n\nНачало диапазона: '))
fin = int(input('Конец диапазона: '))

size = int(input('Введите количество переменных: '))
X = int(input('Какое число вы хотите обнаружить в массиве?\nВведите: '))

A = [random.randint(strt, fin) for i in range(size)]
print(f'\nРандомный массив:\n{A}')

if A[0] <= X: min_diff = X - A[0]
else: min_diff = A[0] - X

near = 0

for i in range(0, len(A)):
    
    if A[i] <= X: diff = X - A[i]
    else: diff = A[i] - X

    if diff < min_diff:
        min_diff = diff
        near = A[i]

print(f'Ближайшим числом к {X}, найденном в массиве является {near}')