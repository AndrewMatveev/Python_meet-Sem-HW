# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: аn = а2 + (n-1) * d. Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# ___________________РЕШЕНИЕ________________________

def input_int_arr():
    while True:
        try:
            arr = []
            for el in input('\nВведите параметры массива в формате: первый элемент, разность, количество элементов \nВвод: ').replace(" ", "").split(','):
                arr.append(int(el))
            return arr
        except ValueError:
            print("Некорректрый ввод. Повторите ввод\n")

def arithm_prog_arr(arr):
    res_arr = [arr[0]]
    for i in range(1, arr[2]):
        res_arr.append(int(res_arr[i - 1] + arr[1])) # здесь вроде как и без int(), но без него не работет иногда
    return res_arr

print(*arithm_prog_arr(input_int_arr()), sep='\n')