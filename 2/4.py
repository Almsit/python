#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры


import sys;

from random import randint

#from msilib import sequence
def valid_inp(inp):
    if(inp.isdigit()):
        return int(inp);
    return False;

def sum_num(ninp1, inp2):

    
    numbers = []
    for i in range(10):
        numbers.append(randint (-10,10))
    print(numbers);
    sum = numbers[inp1 -1]*numbers[inp2 - 1];
    text1 = "произведение ";
    text2 = " * ";
    text3 = " = ";
    return str(text1)+str(numbers[inp1 -1])+str(text2)+str(numbers[inp2 -1])+str(text3)+str(sum);


inp1 = input('Позиция первого элемента от 1 до 10: ');2

inp1 = valid_inp(inp1);
if(inp1 == False):
    print("Ошибка. Неправильное число");
    sys.exit();

inp2 = input('Позиция второго элемента от 1 до 10: ');

inp2 = valid_inp(inp2);
if(inp2 == False):
    print("Ошибка. Неправильное число");
    sys.exit();



print(sum_num(inp1, inp2));
