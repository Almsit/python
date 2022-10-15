#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import sys;

from random import uniform

def valid_inp(inp):
    if(inp.isdigit()):
       return int(inp);
    return False;

inp = input('Введите размер списка ');

inp = valid_inp(inp);

if(inp == False):
    print("Ошибка. Неправильое число");
    sys.exit();


list1 = [round(uniform(0,9),2) for i in range(inp)]

min = min(list1, key=lambda i: float(i))
max = max(list1, key=lambda i: float(i))

dif = (max - int(max)) - (min - int(min))

print(list1)
print(max, min)
print(round(dif,2))