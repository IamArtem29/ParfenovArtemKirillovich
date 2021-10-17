# -*- coding: utf-8 -*-

def fiboSumK():
    N = int(input("Кол-во чисел - "))
    K = int(input("Порядковый номер - "))
    fN = 0
    sN = 1
    summ = 0
    for i in range(2, N):
        contain = sN
        sN = fN + sN
        fN = contain
        if(i >= K - 1 ):
            print(sN)
            summ += sN
    print(summ)
fiboSumK()