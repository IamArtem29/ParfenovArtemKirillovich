# -*- coding: utf-8 -*-

def d3():
    N = int(input("Введите число - "))
    alll = 2
    step = 1
    while alll <= N:
        alll *= 2
        step += 1
    print("Показатель степени", step - 1, "Число", alll // 2)

d3()