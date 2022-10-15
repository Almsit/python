#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
import sys;

def valid_inp(inp):
    if(inp.isdigit()):
       return int(inp);
    return False;

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]

inp = input('Введите число: ');

inp = valid_inp(inp);

if(inp == False):
    print("Ошибка. Неправильое число");
    sys.exit();

for e in range(1, inp + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)