# -*- coding: utf-8 -*-

# 8
def sameN():
    print("3 числа")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    if(n1 == n2 == n3):
        print("Ответ:", 3)
    elif((n1 == n2) or (n3 == n2) or (n1 == n3)):
        print("Ответ:", 2)
    else:
        print("Ответ:", 0)
        
sameN()