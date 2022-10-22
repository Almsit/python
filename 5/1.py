#Напишите программу, удаляющую из текста все слова, содержащие ""абв""
txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"


lst = [];
txt = txt.split(find_txt);

for i in txt:
    lst.append(i)

lst = "".join(lst);
lst = lst.split("  ");

lst2 = "";
for i in lst:
    lst2 += i;
print(f'Результат: {lst2}')