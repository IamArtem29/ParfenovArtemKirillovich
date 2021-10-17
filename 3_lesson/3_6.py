# -*- coding: utf-8 -*-

def fa():
    n = int(input("Факториал - "))
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    print(factor)

fa()