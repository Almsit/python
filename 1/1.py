#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
import sys;

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
    print("Ошибка. Неправильно указан день недели");
    sys.exit();

if(inp >=1 and inp <= 5):
    print("Нет");
else:
    print("Да");