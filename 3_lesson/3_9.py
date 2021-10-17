# -*- coding: utf-8 -*-

def fiboSumm():
    N = int(input("Кол-во чисел - "))
    fN = 0
    sN = 1
    summ = 1
    for i in range(2, N):
        container = sN
        sN = fN + sN
        fN = container
        summ += sN
    print(summ)

fiboSumm()