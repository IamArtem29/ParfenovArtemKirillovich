# -*- coding: utf-8 -*-

def d2():
    i = 2
    N = int(input("Введите число > 2 - "))
    while N % i != 0:
        i += 1
    print("Ответ - ", i)

d2()