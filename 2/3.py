#НЗадайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
import sys;
#from msilib import sequence
def valid_inp(inp):
    if(inp.isdigit()):
        return inp;
    return False;


def sequence(n):
    n = int(n);
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   

inp = input("Введите число:");

inp = valid_inp(inp);
if(inp == False):
    print("Ошибка. Неправильное число");
    sys.exit();

        
print(sequence(inp));
print(sum(sequence(inp)));