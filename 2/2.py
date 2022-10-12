#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import sys;

def valid_inp(inp):
    if(inp.isdigit()):
        return inp;
    return False;

def res_inp(num):
    res = 1;
    arr_res = [];
    for i in range(1, int(num)+1):
        res = int(i)*res;
        arr_res.append(res);
    return arr_res;

inp = input("Введите число:");

inp = valid_inp(inp);
if(inp == False):
    print("Ошибка. Неправильное число");
    sys.exit();

result = res_inp(inp);
print(result);