'''
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

Ввод:                                               Вывод:
print_operation_table(lambda x, y: x * y)           1 2 3 4 5 6
                                                    2 4 6 8 10 12
                                                    3 6 9 12 15 18
                                                    4 8 12 16 20 24
                                                    5 10 15 20 25 30
                                                    6 12 18 24 30 36 
'''

# ___________________РЕШЕНИЕ________________________

def int_input_w_err(text):
    while True: # убрана обработка исключений
        val = input(text)
        if val.isdigit():
            return int(val)
        elif val == '':
            return 6
        print("Некорректный ввод. Повторите ввод\n")

def print_operation_table(operation, num_rows, num_columns):
    
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            print(f"{operation(row, col)}\t", end='')
        print('\n')


x = int_input_w_err('Введите количество строк (по умолчанию 6): ')
y = int_input_w_err('Введите количество столбцов (по умолчанию 6): ')

print_operation_table(lambda x, y: x * y, x, y)