# -*- coding: utf-8 -*-

#3
def voz(age, name):
    if 0 < age < 75 and name != "Иван":
        if age >= 16:
            print('Поздравляем вы поступили в ВГУИТ')
        else:
            print("Сначало нужно окончить школу")
            print("Осталось {} лет".format(16 - age))
    else:
        print("Error")
voz(19, 'Егор')