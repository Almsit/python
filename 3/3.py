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
    print("Ошибка. Неправильное число");
    sys.exit();


list1 = [round(uniform(0,9),2) for i in range(inp)]

min = "None";
max = "None";
for i in list1:
    i = str(i).split(".");
    
    if(min == "None"):
        min = int(i[1]);
    if(max == "None"):
        max = int(i[1]);
    if(min >= int(i[1])):
        min = int(i[1]);
    if(max <= int(i[1])):
        max = int(i[1]);

print(list1)
print(max, min)
print(max - min)