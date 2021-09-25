# -*- coding: utf-8 -*-

# 4
def length():
    a = int(input("a - "))
    b = int(input("b - "))
    l = int(input("l - "))
    N = int(input("N - "))
    print("Ответ:", (2 * N - 1) * a + 2 * l + 2 * (N - 1) * b)
    
length()