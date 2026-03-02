from itertools import count
import math

# def draw_box():
#     for i in range(14):
#         if i != 0 and i != 13:
#             print('*        *')
#         else:
#             print(10 * '*')
#
# draw_box()

# --------------------------

# def draw_triangle():
#     a = ''
#     for i in range(10):
#         a +='*'
#         print(a)
#
# draw_triangle()

# --------------------------
# def print_fio(name, surname, patronymic):
#     print(name[0].upper(), surname[0].upper(), patronymic[0].upper(), sep='')
#
#
# name, surname, patronymic = input(), input(), input()
#
#
# print_fio(surname, name, patronymic)

# --------------------------

# def print_case_counts(s):
#     count_up = 0
#     count_low = 0
#     for i in s:
#         if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or  i in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
#             count_up += 1
#         if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
#             count_low += 1
#         else:
#             continue
#     print('Букв в верхнем регистре:', count_up)
#     print('Букв в нижнем регистре:', count_low)
# s = input()
# 
# print_case_counts(s)

# --------------------------

# def print_digit_sum(num):
#     digit = [int(i) for i in str(num)]
#     print(sum(digit))
#
# num = int(input())
#
# print_digit_sum(num)

# --------------------------

# def print_sorted_hyphen(s):
#     s.sort()
#     print(*s, sep='-')
#
# s = input().split('-')
#
# print_sorted_hyphen(s)

# --------------------------

# def draw_triangle(fill, base):
#     half = base // 2
#
#     for i in range(1, half + 2):
#         print(fill * i)
#
#     for i in range(half, 0, -1):
#         print(fill * i)
#
# fill = input()
# base = int(input())
#
# draw_triangle(fill, base)

# --------------------------
# def print_perm_time_call(msc_time):
#     count = []
#
#     for i in range(len(msc_time)):
#
#         count = int((msc_time[0])) + 2
#     print(f'Созвон будет в {str(count).zfill(2)}:{msc_time[1]}.')
#
# msc_time = input().split(':')
#
# print_perm_time_call(msc_time)

# --------------------------
#
# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
# print(get_sum(1, 2, 3))

# --------------------------

# def convert_to_miles(km):
#     miles = km * 0.6214
#     return miles
#
# km = int(input())
#
# print(convert_to_miles(km))

# --------------------------

# def code_format(text):
#     tegs = '<code>' + text + '</code>'
#     return tegs
#
# text = input()
#
# print(code_format(text))

# --------------------------
# def get_days(day_month):
#     if day_month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif day_month in (4, 6, 9, 11):
#         return 30
#     else:
#         return 28
#
# print(get_days(int(input())))

# --------------------------

# def math_round_to_int(num):
#     if int(num * 10) % 10 >= 5:
#         return math.ceil(num)
#     else:
#         return round(num)
#
# print(math_round_to_int(float(input())))

# --------------------------

# def get_factors(num):
#     counter = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter.append(i)
#     return counter
#
# print(get_factors(int(input())))

# --------------------------

# def number_of_factors(num):
#
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     return counter
#
# print(number_of_factors(int(input())))

# --------------------------

# def get_unique(numbers):
#     counter =[]
#     for i in range(len(numbers)):
#         if numbers[i] not in counter:
#             counter.append(numbers[i])
#     return counter
#
# print(get_unique(eval(input())))

# --------------------------

# def get_last_index(data, value):
#     count = -1
#     for i in range(len(data)):
#         if value == data[i]:
#             count = i
#
#     if count == -1:
#         return 'ERROR!'
#
#     return count
#
# data = eval(input())
# value = eval(input())
#
# print(get_last_index(data, value))

# --------------------------

# def find_all(target, symbol):
#     count_sym = []
#     for i in range(len(target)):
#         if symbol == target[i]:
#             count_sym.append(i)
#     return count_sym
#
# print(find_all(input(), input()))

# --------------------------

# def merge(list1, list2):
#     list1.extend(list2)
#     list1.sort()
#     return list1
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# print(merge(numbers1, numbers2))

# --------------------------
#
# def quick_merge():
#     n = int(input())
#     list1 =[]
#     for _ in range(n):
#         row = [int(c) for c in input().split()]
#         list1.extend(row)
#     list1.sort()
#     return list1
#
# print(*quick_merge())

# --------------------------

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# if is_even(int(input())):
#     print('Это число чётное.')
# else:
#     print('Это число нечётное.')

# --------------------------

# def is_valid_triangle(side1, side2, side3):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
#
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))

# --------------------------

def is_palindrome(text):
    text = ''.join(e for e in text if e.isalnum())

    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome(input().lower()))