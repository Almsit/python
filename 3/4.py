#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
import sys;

def valid_inp(inp):
    if(inp.isdigit()):
       return int(inp);
    return False;


inp = input('Введите число: ');

inp = valid_inp(inp);

if(inp == False):
    print("Ошибка. Неправильое число");
    sys.exit();

num = ''
while inp > 0:
    num = str(inp % 2) + num
    inp = inp // 2
print(f'Двоичное число: {num}')