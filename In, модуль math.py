import math



# s = input()
#
# if "синий" in s:
#     print("YES")
# else:
#     print("NO")


# email = input()
#
# if "@" in email and "." in email:
#     print("YES")
# else:
#     print("NO")


# num1 = math.sqrt(2)     # вычисление квадратного корня из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)


# from math import * // Однако рекомендуется избегать импортирования через from math import *,
# так как нет ясности, какие функции были импортированы и это загрязняет пространство имён лишними, неиспользуемыми функциями.
# Вместо этого рекомендуется использовать from math import sqrt или import math, чтобы явно указать, что именно вы импортируете.
# Это делает ваш код более читаемым и управляемым.

# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# import math
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
#
# dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
#
# p = math.sqrt(dis)
#
# print(p)

# a = float(input())
# b = float(input())
#
# ar = (a + b) / 2
# geo = math.sqrt(a * b)
# gar = 2 * (a * b) / (a + b)
# kva = math.sqrt((a ** 2 + b ** 2) / 2)
#
# print(ar, "\n", geo, "\n", gar, "\n", kva, sep="")


# пол и потолок
# x = float(input())
#
# x1 = math.floor(x)
# x2 = math.ceil(x)
#
# print(x1 + x2)


# Квадратное уравнение

# a = float(input())
# b = float(input())
# c = float(input())
#
# d = (b ** 2) - (4 * a * c)
#
#
# if d > 0:
#     x1 = (-b - math.sqrt(d)) / (2 * a)
#     x2 = (-b + math.sqrt(d)) / (2 * a)
#     print(min(x1,x2))
#     print(max(x1,x2))
# elif d == 0:
#     x = -b / (2 * a)
#     print(x)
# elif d < 0:
#     print("Нет корней")

# Правильный многоугольник

n = float(input())
a = float(input())

s = (n * a ** 2) / (4 * math.tan(math.pi / n))

print(s)

