from itertools import count


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









