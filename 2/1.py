#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import sys;

def valid_inp(inp):
    inp = inp.replace(".", "");
    if(inp.isdigit()):
        return inp;
    return False;

def sum_inp(num):
    res = 0;
    for i in num:
        res += int(i);
    return res;

inp = input("Введите число:");

inp = valid_inp(inp);
if(inp == False):
    print("Ошибка. Неправильное число");
    sys.exit();

result = sum_inp(inp);
print(result);