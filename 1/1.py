#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
import sys;
'''
def valid_inp(inp):
    if(inp.isdigit()):
        inp = int(inp);
        if(inp >= 1 and inp <= 7):
            return inp;
    return False;

week_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"];
week_inp = input("Введите день недели от 1 до 7 (цифра):");

inp = valid_inp(week_inp);
if(inp == False):
    print("Нет");
    sys.exit();
print("Да");

'''


'''
#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def input_numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = input_numbers(3)

if check_predicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

'''

'''
#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


def input_coord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Error! Введите пожалуйста числа!")
    return a

def check_coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = input_coord(2)
check_coordinates(koordinate)

'''




'''
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

'''

'''
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 

def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculate_length_segment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = input_numbers(2)
print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {format(calculate_length_segment(pointA, pointB), '.2f')}")
'''