# -*- coding: utf-8 -*-

# 9
def chocolate():
    print("n, m, k")
    n = int(input())
    m = int(input())
    k = int(input())
    if(n * m > k and (k % m == 0 or k % n == 0)):
        print("Ответ: Да")
    else:
        print("Ответ: Нет")

chocolate()