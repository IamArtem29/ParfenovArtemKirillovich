# -*- coding: utf-8 -*-

def countF():
    string = input("Строка - ")
    if (string.count("f") == 1):
        print(string.find("f"))
    if (string.count("f") >= 2):
        print("Первый - ", string.find("f"))
        print("Последний - ", string.rfind("f"))
    
countF()