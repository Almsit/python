
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def valid_inp(inp):
    if(inp.isdigit()):
       return int(inp);
    return False;

inp = input('Введите размер списка ');

inp = valid_inp(inp);

i = 2 # первое простое число
lst = []
old = inp
while i <= inp:
    if inp % i == 0:
        lst.append(i)
        inp //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")