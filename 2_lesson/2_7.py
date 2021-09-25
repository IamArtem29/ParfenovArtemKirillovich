# -*- coding: utf-8 -*-

# 7
def yearV():
    print("Год")
    year = int(input())
    if( (year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print("Ответ: Да")
    else:
        print("Ответ: Нет")
        
yearV()