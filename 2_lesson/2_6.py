# -*- coding: utf-8 -*-

def chess():
    print("4 координаты")
    a1 = int(input())
    a2 = int(input())
    b1 = int(input())
    b2 = int(input())
    if( (1 <= a1 <= 8) and (1 <= a2 <= 8) and (1 <= b1 <= 8) and (1 <= b2 <= 8) ):
        if( ( (a1 % 2 != 0) and (a2 % 2 != 0) ) or ( (a1 % 2 == 0) and (a2 % 2 == 0) ) ):
            fc = "black"
        else:
            fc = "white"
        if( ( (b1 % 2 != 0) and (b2 % 2 != 0) ) or ( (b1 % 2 == 0) and (b2 % 2 == 0) ) ):
            sc = "black"
        else:
            sc = "white"
        if(fc == sc):
            print("Ответ: Да")
        else:
            print("Ответ: Нет")

chess()