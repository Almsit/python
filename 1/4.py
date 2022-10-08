import sys;

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def valid_inp(inp):
    if(inp.isdigit()):
        inp = int(inp);
        if(inp >= 1 and inp <= 7):
            return inp;
    return False;

quarter = input('Введите номер четверти: ')

inp = valid_inp(quarter);
if(inp == False):
    print("Ошибка");
    sys.exit();
if inp == 1:
    print('x > 0, y > 0')
elif inp == 2:
    print('x < 0, y > 0')
elif inp == 3:
    print('x < 0, y < 0')
elif inp == 4:
    print('x > 0, y < 0')
else:
    print('На координатной плоскости только 4 четверти')

