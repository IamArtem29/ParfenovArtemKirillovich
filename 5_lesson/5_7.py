# -*- coding: utf-8 -*-

def d7():
    numb = 0
    loop_first = True
    while True:
        x = int(input("Число - "))
        if x == 0:
            break
        if(loop_first != True):
            if(x > container):
                numb += 1
        container = x
        loop_first = False
    print(numb)

d7()