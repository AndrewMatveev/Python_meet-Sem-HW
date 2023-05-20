# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2,1, 4, -2,10, 2, 0, -9, 8,10, -9, 0,-5,-5, 7]
# Вывод: [1, 9,13,14,19]

import random

def int_input_w_err(text):
    while True:
        try:
           print(text, end='')
           val = int(input())
           return val
        except ValueError:
            print("Некорректрый ввод. Повторите ввод\n")


def filter_array(array, min_val, max_val):
    filtered_array = []
    for i in array:
        if min_val <= i <= max_val:
            filtered_array.append(i)
    return filtered_array


strt = int(input('\nВведите дипазон генерации ниже\nНачало диапазона: '))
fin = int(input('Конец диапазона: '))
N = int(input('Введите количество переменных: \n'))


min = int_input_w_err('Введите минимум: ')
max = int_input_w_err('Введите максимум: ')


print('\nСгенерированный массив: ', arr := [random.randint(strt, fin) for i in range(N)])

print('\nОтфильтрованный массив: ', filter_array(arr, min, max))