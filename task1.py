# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def Number_increase (number, quantity):
    result = number
    if quantity == 1: 
        return result
    else:
        for _ in range(quantity):
            result = number * quantity
        return result

n = input("Введите число: ")
res = 0
for i in range(1, 4):
    res += int(Number_increase(n, i))
print(f"Результат: {res}")