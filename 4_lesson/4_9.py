# -*- coding: utf-8 -*-

def del_character():
    string = input("Строка - ")
    ch_del = input("Del - ")
    print(string.replace(ch_del, ""))

del_character()