# -*- coding: utf-8 -*-

def sumN():
    sum = 0
    for i in range(int(input("кол-во чисел - "))):
        sum += int(input("число - "))
    print(sum)

sumN()