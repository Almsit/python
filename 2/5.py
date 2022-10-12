#Реализуйте алгоритм перемешивания списка.
import sys;
import random;


def arr_sort(arr):
    rand = random.randint(0, len(arr)-1);
    arr_temp.append(arr[rand]);
    del arr[rand];
    if(len(arr) > 0):
        arr_sort(arr);
    else:
        return arr_temp;
    
arr = [];
arr_temp = [];

for i in range(0, 10):
    arr.append(i);

    
arr_sort(arr);
print(arr_temp);