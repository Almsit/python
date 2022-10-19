#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import sys;

def valid_inp(inp):
    check = 0;12
    for i in inp:
        if(i.isdigit() == False):
            check = 1;
    if(check == 0):
        return inp;
    return False;

inp = input("Введите числа ");

str_arr = valid_inp(inp);

if(str_arr == False):
    print("Ошибка. Неправильный набор чисел");
    sys.exit();

str_res = "";
arr = [];

for i in str_arr:
    if(str_arr.count(i)== 1):
        str_res += i;
        arr.append(i);

print(arr);