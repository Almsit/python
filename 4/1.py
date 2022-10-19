#Вычислить число Пи c заданной точностью d
import math
list_val = ["0.001", "0.1", "0.00001"];
n = math.pi;
for i in list_val:
    i = len(str(i).split(".")[1]);
    print("{:.{p}f}".format(n, p=i))   
