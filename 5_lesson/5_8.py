# -*- coding: utf-8 -*-

def d8():
    numb = 1
    maxStreak = 0
    loop_first = True
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if(loop_first != True):
            if(x == container):
                numb += 1
            else:
                if(maxStreak < numb):
                    maxStreak = numb
                numb = 1
        container = x
        loop_first = False
    print(max(maxStreak, numb))

d8()