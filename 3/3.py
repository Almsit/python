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
i_temp = 0;
for i in list1:
    i = str(i).split(".");
    if(len(i[1]) == 1):
        i_temp = int(i[1])*10;
    else:
        i_temp = int(i[1]);

    if(min == "None"):
        min = i_temp;

    if(max == "None"):
        max = i_temp;

    if(min >= i_temp):
        min = i_temp;

    if(max <= i_temp):
        max = i_temp;

'''
    if(len(i[1])>1):
        i_temp = round(int(i[1])/10, 2);
    else:
        i_temp = int(i[1]);
    

    if(min == "None"):
        min = i_temp;
    if(max == "None"):
        max = i_temp;

    if(min >= i_temp):
        min = i_temp;

    if(max <= i_temp):
        max = i_temp;

'''
print(list1)
print(max, min)
print(max - min)