# -*- coding: utf-8 -*-

def f_second():
    string = input("Строка - ")
    if (string.count("f") == 1):
        print(-1)
    elif (string.count("f") == 0):
        print(-2)
    else:
        print(string.find("f", string.find("f") + 1))

f_second()