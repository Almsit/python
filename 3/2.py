#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random;

def result(arr):
    if(len(arr)>1):
        arr2.append(arr[0]*arr[len(arr)-1]);
        arr.pop(0);
        arr.pop(len(arr)-1);
        result(arr);
    else:
        return arr2;

arr = [];
arr2 = [];

for i in range(random.randint(5, 20)):
    rand = random.randint(2, random.randint(2, 10));
    arr.append(rand);

print(arr);
result(arr);
if(len(arr) == 1):
    print("Остаток - ", arr[0]);

print(arr2);


