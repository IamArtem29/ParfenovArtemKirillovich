# -*- coding: utf-8 -*-

def d4():
    x = int(input("Введите первое число - "))
    y = int(input("Введите второе число - "))
    numb = 1
    while x < y:
        x *= 1.1
        numb += 1
    print(numb)

d4()