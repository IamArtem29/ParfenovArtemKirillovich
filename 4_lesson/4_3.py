# -*- coding: utf-8 -*-

def split_s():
    string = input("Строка - ")
    lenght = len(string) // 2 + len(string) % 2
    p_1 = string[0:lenght]
    p_2 = string[lenght:]
    print(p_2 + p_1)

split_s()