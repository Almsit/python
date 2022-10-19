#Вычислить число Пи c заданной точностью d
import sys;
import math
from math import factorial
from decimal import Decimal


inp = input('Введите число в формате от 0.1 - до 0.000000000001 ');

def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)          
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi

#print(calc(25));
n = str(calc(25)).split(".");

k = 0;
res = "";
while k<len(inp)-2:
    res += n[1][k];
    k += 1;
res = str(n[0])+"."+res;
print(res)
