# -*- coding: utf-8 -*-

def del_bh():
    string = input("Строка - ")
    string = string[:string.find('h')] + string[string.rfind('h') + 1:]
    print(string)

del_bh()