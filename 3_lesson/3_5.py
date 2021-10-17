# -*- coding: utf-8 -*-

def fN():
    n = int(input("Число - "))
    sumN = 0
    for i in range(n + 1):
        sumN += i ** 3
    print(sumN)

fN()