import math

print("Введите коэффициенты квадратного уравнения:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d= b * b - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Корни уравнения:", "\nx1 =", x1, "x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("Корень уравнения:", "\nx = ", x)
else:
    print("Корней нет")
