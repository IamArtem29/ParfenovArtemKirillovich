# -*- coding: utf-8 -*-

def d6():
    k_num = 0
    summ = 0
    while True:
        x = int(input("Число - "))
        if x == 0:
            break
        k_num += 1
        summ += x
    print(summ / k_num)

d6()