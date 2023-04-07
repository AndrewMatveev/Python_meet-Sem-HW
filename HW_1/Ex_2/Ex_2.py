# # Задача 2: Найдите сумму цифр трехзначного числа

# Пример
# 100 -> 1 (1 + 0 + 0)


# ___________________DECISION____________________

num = int(input("Insert integer 3-digit number: "))

if abs(num) < 100:
    print("Inserted number is't 3-digit")
else:
    res = num % 10 + num // 10 % 10 + num // 100 % 10
    print(f"Sum digits of number is {res}")

# _______________________________________________