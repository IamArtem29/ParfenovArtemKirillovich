# -*- coding: utf-8 -*-

# 3
def timeDay():
    time = int(input("Кол-во минут прошло - "))
    if time < 1440:
        h = time // 60
        m = time % 60
        print("Ответ:", str(h % 24) + ":" + str(m))
    else:
        print("Error")
timeDay()