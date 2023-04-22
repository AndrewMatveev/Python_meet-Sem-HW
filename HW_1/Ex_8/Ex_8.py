# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).



# ___________________РЕШЕНИЕ ЗДОРОВОГО ЧЕЛОВЕКА___________________________

n = int(input("Введите длинну (n) шоколадки: "))
m = int(input("Введите ширину (m) шоколадки: "))


piece = int(input("Какого размера кусочек вы хотите отломить?\nВведите: "))

if piece < m * n and (piece % m == 0 or piece % n == 0):
    print("Ломай!")
else:
    print("За один раз не выйдет")

# ________________________________________________________________________




# ___________________РЕШЕНИЕ КУРИЛЬЩИКА___________________________________
"""

n = int(input("Введите длинну (n) шоколадки: "))
m = int(input("Введите ширину (m) шоколадки: "))

print("Какого размера кусочек вы хотите отломить?")
piece = int(input("Введите: "))

test = int(0)

for i in range(1, m):
    if piece == n * i:
        test += 1
    else:
        for j in range(1, n):
            if piece == j * m:
                test += 1

if test > 0:
    print("Ломай!")
else:
    print("За один раз не выйдет")
    
"""
# ________________________________________________________________________