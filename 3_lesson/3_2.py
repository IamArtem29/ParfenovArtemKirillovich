# -*- coding: utf-8 -*-

def prAB():
    A = int(input("1 = "))
    B = int(input("2 = "))
    if(A < B):
        for i in range(A, B + 1):
            print(i)
    else:
        for i in range(A, B - 1, -1):
            print(i)
prAB()