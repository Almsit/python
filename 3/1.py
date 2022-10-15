#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import sys;

def valid_inp(inp):
    check = 0;
    for i in inp:
        if(i.isdigit() == False):
            check = 1;
    if(check == 0):
        return inp;
    return False;

def sum(arr):
    k = 0;
    res = 0;
    for i in arr:
        if(k == 0):
            k += 1;
        else:
            res += int(i);
            k -= 1;
    return res;


inp = input("Введите числа через пробел:").split();

arr = valid_inp(inp);

if(arr == False):
    print("Ошибка. Неправильный набор чисел");
    sys.exit();

print(sum(arr));


