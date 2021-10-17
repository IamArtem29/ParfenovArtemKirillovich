# -*- coding: utf-8 -*-

n = int(input("Число - "))

def fSumm(n):
    x = n
    factorial = 1
    summ = 0
    for i in range(1, x + 1):
        factorial *= i
        summ += factorial
    print("Ответ -", summ)

fSumm(n)