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

# s = input()
#
# print(s[:3][-1:])
# print(s[-2:][0:1])
# print(s[:5])
# print(s[:-2])
# print(s[0::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])


# s = input()
# l = len(s) + 1
# part1 = s[0:l// 2]
# part2 = s[l//2:]
#
# print(part2 + part1)

# s = input()
#
# if s == s.title():
#     print('YES')
# else:
#     print('NO')


# s = input()
# string = s.swapcase()
# print(string)

# print(input().swapcase())

#
# s = input()
# a = 'хорош'
#
# if a in s.lower():
#     print('YES')
# else:
#     print('NO')

# s = input()
# count = 0
#
# for i in range(len(s)):
#     if  s[i].islower():
#         count +=1
# print(count)
#
# s = input()
# count = 0
#
# for i in s:
#     if i.lower() != i:
#         count += 1
#
# print(count)

# s = input()
# print(s.count(' ') + 1)

# s = input()
# str = s.lower()
# print('Аденин:', str.count('а'))
# print('Гуанин:', str.count('г'))
# print('Цитозин:', str.count('ц'))
# print('Тимин:', str.count('т'))


# n = int(input())
# count = 0
# for i in range(n):
#     s = input()
#     if s.count('11') > 2:
#         count +=1
#
# print(count)

# s = input()
# count = 0
#
# for i in range(len(s)):
#     if s[i] in '1234567890':
#         count += 1
# print(count)

# s = input()
#
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

#
# s = input()
# counter = 0
# counter1 = ''
#
# for i in s:
#     if s.count(i) >= counter:
#         counter = s.count(i)
#         counter1 = i
# print(counter1)

#
# s = input()
# count = 0
# for i in s:
#     if i == 'f':
#         count += 1
# if count == 1:
#     print(s.find('f'))
#
# if count > 1:
#     print(s.find('f'), end=' ')
#     print(s.rfind('f'))
#
# if count == 0:
#     print('NO')

# s= input()
# if s.find('f') == -1:
#     print('NO')
# elif s.find('f') == s.rfind('f'):
#     print(s.find('f'))
# else:
#     print(s.find('f'),s.rfind('f'))


# s = input()
#
# for i in range(len(s)):
#     if i == s.find('h'):
#         print(s[:i], end='')
#     if i == s.rfind('h'):
#         print(s[i+1:])



# n = int(input())
#
# for i in range(1, n + 1):
#     comment = input()
#     if len(comment) == 0:
#         print(i, ':', ' ', 'COMMENT SHOULD BE DELETED', sep='')
#     elif comment.isspace():
#         print(i,':',' ', 'COMMENT SHOULD BE DELETED', sep='')
#     else:
#         print(i,':',' ', comment, sep='')





















