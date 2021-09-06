# -*- coding: utf-8 -*-

#1
print("Курс Основы программирования начался")

#2
print(16823 * 12302 % 3092)

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

#4
seconds = 111111
days = seconds // 86400
seconds = seconds  - 86400 * days
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes  * 60
print(days, hours, minutes, seconds)

#5
n = 4
print(n + n**2 + n**3 + n**4 + n**5)

#6
x = 0
y = 1
x, y = y, x
print(x, y)

#7
num = 5
if num % 2 == 0:
    print("true")
else:
    print('false')