# -*- coding: utf-8 -*-

def lad():
    n = int(input("Число 1 - 9 = "))
    if 1 <= n <= 9:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, sep = "", end= "")
            print()
    else:
        print("Error")

lad()