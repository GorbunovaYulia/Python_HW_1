"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
number = int(input("Введите число"))
sum = 0
thirdNumber = number % 10
firstNumber = number//100
secondNumber = number//10 % 10
print(thirdNumber+firstNumber+secondNumber)
