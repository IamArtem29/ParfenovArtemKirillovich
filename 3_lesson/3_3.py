# -*- coding: utf-8 -*-

def ubAB():
    A = int(input("1 = "))
    B = int(input("2 = "))
    for i in range(A, B - 1, -1):
        if i % 2!= 0:
            print(i)
ubAB()