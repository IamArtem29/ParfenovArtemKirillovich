# -*- coding: utf-8 -*-

def rev():
    string = input("Строка - ")
    a = string.find("h")
    b = string.rfind("h")
    print(string[:a + 1] + string[a + 1:b][::-1] + string[b:])

rev()