import math
from itertools import count

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# for i in range(len(s)):
#     if s[i] == 'w':
#         print(i)
#         break

# s = input()
#
# for i in range(len(s)-1, -1, -1):
#     print(s[i])


# name = input()
# ser = input()
# last_name = input()
#
# print(ser[0], name[0],last_name[0], sep='')


# animals = input()
# count = 0
# for i in range(len(animals)):
#     count+=1
#     print(count,')', ' ', animals[i], sep='')

# s = input()
# n = 0
# for i in range(len(s)):
#     n += int(s[i])
# print(n)

# s = input()
# flag = True
# for i in range(len(s)):
#
#     if s[i] in '0123456789':
#         flag = False
# if flag == False:
#     print('Цифра')
# else:
#     print('Цифр нет')

# s = input()
# digits = '0123456789'
#
# for c in s:
#     if c in digits:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')


# s = input()
# count = 0
# count1 = 0
# for i in range(len(s)):
#     if s[i] in '+':
#         count +=1
#     if s[i] in '*':
#         count1 +=1
# print(f"Символ + встречается {count} раз")
# print(f"Символ * встречается {count1} раз")


# s = input()
# glas = 'ауоыиэяюеАУОЫИЭЯЮЕ'
# so_glas = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
# count = 0
# count1 = 0
# for i in s:
#     if i in glas:
#         count += 1
#     if i in so_glas:
#         count1 += 1
#
# print('Количество гласных букв равно', count)
# print('Количество согласных букв равно',count1)


# s = input()
# count = 0
#
# for i in s:
#     if i in '+':
#         count += 1
#
# print(f"Символ + встречается {count} раз")


# s = input()
#
# count = 0
# num = ' '
# for i in range(len(s)):
#     if num in s[i]:
#         count += 1
#     num = s[i]
# print(count)


# s = int(input())
# count = 0
# while s > 0:
#     n = s % 2
#     print(str(n), end='')
#     s = s // 2


# s = int(input())
# count = ''
# a = ''
# while s > 0:
#     n = s % 2
#     count = str(n)
#     a += count
#     s = s // 2
#
# print(a[::-1])
#
# s = input()
#
# if s[::1] == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# print(len(s))
# print(s * 3)
# print(s[:1])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:][:-1])






