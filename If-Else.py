import pdb

from math import *
from calendar import monthrange

# num1, num2, num3 = int(input()), int(input()), int(input())
#
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
#
# print(counter)


# num1 = int(input())
#
# a = num1 //1 % 10
# b = num1 //10 % 10
# c = num1 //100 % 10
# d = num1 //1000 % 10
#
# if a + d == c - b:
#     print("ДА")
# else:
#     print("НЕТ")


# age = int(input())
#
# if 0 <= age <= 13:
#     print("детство")
# elif 14 <= age <= 24:
#     print("молодость")
# elif 25 <= age <= 59:
#     print("зрелость")
# else:
#     print("старость")


# x = int(input())
#
# if (10000 > x > 999) and (x % 7 == 0 or x % 17 == 0):
#     print("YES")
# else:
#     print("NO")

# ЗАДАЧА С ВИСОКОСНЫМ ГОДОМ
# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")


# x = int(input())
# y = int(input())
# x1 = int(input())
# y1 = int(input())
#
# if  (x + 1 >= x1 or x - 1 <= x1) and (y + 1 >= y1 or y - 1 <= y1):
#     print("YES")
# else:
#     print("NO")

#
# z_n, f_k = int(input()), int(input())
#
# if z_n > f_k:
#     print("NO")
# elif f_k > z_n:
#     print("YES")
# else:
#     print("Don't know")

# weight = int(input())
#
# if weight < 60:
#     print("Легкий вес")
# elif 60 <= weight < 64:
#     print("Первый полусредний вес")
# elif 64 <= weight < 69:
#     print("Полусредний вес")

# КАЛЬКУЛЯТОР
# num1 = int(input())
# num2 = int(input())
# string = input()
#
# if string == "+":
#     print(num1 + num2)
# elif string == "-":
#     print(num1 - num2)
# elif string == "*":
#     print(num1 * num2)
# elif string == "/":
#         if num2 == 0:
#             print("На ноль делить нельзя!")
#         else:
#             print(num1 / num2)
# else:
#     print("Неверная операция")

# col1 = input()
# col2 = input()
#
# if (col1 != "красный" and col1 != "желтый" and col1 != "синий") or (col2 != "красный" and col2 != "желтый" and col2 != "синий"):
#     print("ошибка цвета")
#
# elif col1 == "красный" and col2 == "синий" or col1 == "синий" and col2 == "красный":
#     print("фиолетовый")
#
# elif col1 == "красный" and col2 == "желтый" or col1 == "желтый" and col2 == "красный":
#     print("оранжевый")
#
# elif col1 == "синий" and col2 == "желтый" or col1 == "желтый" and col2 == "синий":
#     print("зеленый")
#
# elif col1 == col2:
#     print(col1)


# digit = int(input())
#
# if digit == 1:
#     print("I")
# elif digit == 2:
#     print("II")
# elif digit == 3:
#     print("III")
# elif digit == 4:
#     print("IV")
# elif digit == 5:
#     print("V")
# elif digit == 6:
#     print("VI")
# elif digit == 7:
#     print("VII")
# elif digit == 8:
#     print("VIII")
# elif digit == 9:
#     print("IX")
# elif digit == 10:
#     print("X")
# else:
#     print("ошибка")


# number = int(input())
#
# if not number % 2 == 0:
#     print("YES")
# elif number % 2 == 0 and 2 <= number <= 5:
#     print("NO")
# elif number % 2 == 0 and 6 <= number <= 20:
#     print("YES")
# elif number % 2 == 0 and number > 20:
#     print("NO")


# x = int(input())
#
# if x == 0:
#     print("зеленый")
# elif 1 <= x <= 10:
#     if x % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 11 <= x <= 18:
#     if x % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# elif 19 <= x <= 28:
#     if x % 2 == 0:
#         print("черный")
#     else:
#         print("красный")
# elif 29 <= x <= 36:
#     if x % 2 == 0:
#         print("красный")
#     else:
#         print("черный")
# else:
#     print("ошибка ввода")









