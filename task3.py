# Задача 3. Найдите все простые несократимые дроби, 
# лежащие между 0 и 1, знаменатель которых не превышает 11.

def Check_divisibility(numerals, denominator):
    if numerals < 2:
        return True
    for i in range(2, denominator + 1):
        if numerals % i == 0 and denominator % i == 0:
            return False
    return True

fractions = []

for denominator in range (2, 12):
    for numerals in range(1, denominator):
        if Check_divisibility(numerals, denominator):
            fractions.append(str(numerals) + "/" + str(denominator))
            
print("Несократимые дроби:")
print(", ".join(fractions))