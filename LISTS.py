from itertools import count, chain
from operator import length_hint
from re import split
from symbol import continue_stmt

#
# n = input()
# c = ''
# numbers = list(n)
#
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         c += numbers[i]
# print(list(c))

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
#
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
#
# print(rainbow)

# ---------------------------------
# alf = 'abcdefghijklmnopqrstuvwxyz'
# count = ['a']
# for i in range(1, len(alf)):
#     count.append(alf[i] * (i + 1))
#
# print(count)

# ---------------------------------
# n = int(input())
# lst = []
# for i in range(n):
#     str = input()
#     lst.append(str)
# print(lst)

# -----------------------------

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11,
#            10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
#
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)

# ----------------

# n = int(input())
# lst = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         lst.append(i)
# print(lst)

# -----------------

# n = int(input())
# lst = []
# numbers = int(input())
# for i in range(n-1):
#     count = numbers
#     numbers = int(input())
#     lst.append(numbers + count)
# print(lst)

# -------------------

# n = int(input())
# lst = []
# for i in range(n):
#     number = int(input())
#     lst.append(number)
# del lst[1::2]
# print(lst)

# -------------------

# n = int(input())
# lst = []
# s = ''
# s1 = ''
# for i in range(n):
#      str = input()
#      lst.append(str)
# k = int(input())
# for h in range(len(lst)):
#      s = lst[h]
#      if k <= len(s):
#         s1 += s[k-1]
#      else:
#          continue
# print(s1)

# -----------------------

# n = int(input())
# lst = []
# for _ in range(n):
#     s = input()
#     lst.extend(s)
# print(lst)

# --------------------

# n = int(input())
# count = []
# count1 = []
# for i in range(n):
#     x = int(input())
#     count.append(x)
#     f = x ** 2 + 2 * x + 1
#     count1.append(f)
#
# print(*count, sep='\n')
# print()
# print(*count1, sep='\n')

# -----------------------

# n = int(input())
# count = []
#
# for i in range(n):
#     num = int(input())
#     count.append(num)
# count.remove(max(count))
# count.remove(min(count))
#
# print(*count, sep='\n')

# ----------------------------

# n = int(input())
# count = []
#
# for i in range(n):
#     str = input()
#     if str not in count:
#         count.append(str)
#
# print(*count, sep='\n')


# -------------------------

# n = int(input())
# stringi = []
# res = []
# reg = []
# count = []
#
# for i in range(n):
#     text = input()
#     stringi.append(text)
#
# k = int(input())
# for j in range(k):
#     request = input()
#     reg.append(request.lower())
#
# for h in range(len(stringi)):
#     for r in reg:
#         if r not in stringi[h].lower():
#             break
#     else:
#         count.append(stringi[h])
#
# print(*count, sep='\n')

# -------------------------


# n = int(input())
# count_minus = []
# count_zero = []
# count_plus = []
# for i in range(n):
#     num_1 = int(input())
#     if num_1 < 0:
#         count_minus.append(num_1)
#     if num_1 == 0:
#         count_zero.append(num_1)
#     if num_1 > 0:
#         count_plus.append(num_1)
#
# print(*count_minus, sep='\n')
# print(*count_zero, sep='\n')
# print(*count_plus, sep='\n')


# ----------------------

# str = input()
# str1 = str.split()
#
# for i in str1:
#     print(i[0] + '.', end='')

# -----------------------------

# str = input()
#
# str1 = str.split('\\')
#
# print('\n'.join(str1))

# -----------------------------

# num = input().split('.')
# count = 0
# for i in range(len(num)):
#     num[i] = int(num[i])
#     if 0 <= num[i] <= 255:
#         count += 1
#
# if count == 4:
#     print('ДА')
# else:
#     print('НЕТ')

# ------------------------------

# str = input()
# separator = input()
# str1 = separator.join(str)
#
# print(str1)

# -------------------------


# s = input().split()
# count = 0
#
# for i in range(len(s)):
#     for h in range(i + 1, len(s)):
#         if s[i] == s[h]:
#             count += 1
#
# print(count)

# ---------------------

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# numbers.pop(0)
# numbers.extend(numbers)
# numbers.insert(3, 25)
# print(numbers)

# --------------------

# s = input().lower()
#
# s1 = s.split()
# counter = s1.count('a')
# counter1 = s1.count('an')
# counter2 = s1.count('the')
#
# total = counter + counter1 + counter2
#
# print('Общее количество артиклей:', total)

# --------------------

# str_num = input().split()
# int_num = []
# for i in range(len(str_num)):
#     int_num.append(int(str_num[i]))
#
# index_max = int_num.index(max(int_num))
# index_min = int_num.index(min(int_num))
#
#
# int_num[index_max], int_num[index_min] = int_num[index_min], int_num[index_max]
#
# print(*int_num)

# --------------------

# num_str = input().split()
#
# int_num = []
#
# for i in range(len(num_str)):
#     int_num.append(int(num_str[i]))
#
# int_num.sort()
# print(*int_num)
# int_num.sort(reverse=True)
# print(*int_num)

# --------------------

# n = int(input())
# songs = []
#
# for i in range(n):
#     song = input()
#     songs.append(song)
#
# songs.sort()
# print(*songs, sep='\n')
# print('\n'.join(songs))

# --------------------


# string = (input())
# string.split()
# n = int(string[1:])
#
# counter = []
# for i in range(n):
#     text = input()
#     if '#' in text:
#         text = text[0: text.find('#')]
#     text = text.rstrip()
#     counter.append(text)
#
# print(*counter, sep='\n')

# --------------------


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class',
#             'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for',
#             'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#             'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [i for i in keywords if len(i) >= 5]
#
# print(lengths)

# --------------------

# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# --------------------

# squere = [i ** 2 for i in range(1, int(input())+1)]
#
# print(*squere, sep='\n')


# --------------------

# stringi = input().split()
# c = []
# for i in stringi:
#     c.append(int(i) ** 3)
#
# print(*c)
#  то же через списочное выражение

# cube =  [int(i) ** 3 for i in input().split()]
#
# print(*cube)

# --------------------

# s = input()
# c = []
# for i in s:
#     if i in '0123456789':
#         c.append(i)
#
# print(*c, sep='')

# то же через списочное выражение
# number_only = [ i for i in input() if i in '0123456789']
#
# print(*number_only, sep='')

# --------------------

# quare = [ int(i) ** 2 for i in (input().split()) if int(i) % 2 == 0 and (int(i)**2) % 10 != 4]
#
# print(*quare)

# --------------------
# n = (input()).split()
#
# n1 = (input()).split()
# c = []
#
# for i in range(len(n)):
#     for g in range(len(n)):
#         if i == g:
#             c.append(int(n[i]) + int(n1[g]))
#
# print(c)

# --------------------

# n = (input()).split()
# summa = 0
#
# for i in range(len(n)):
#     summa += int(n[i])
#
# n1 = [int(i) for i in range(len(n))]
#
# print(*n, sep='+', end='=')
# print(summa)


# --------------------

# n = input().split()
#
# length = [len(n[i]) for i in range(len(n))]
#
# print(max(length))

# --------------------

# c = [i[1:] + i[0] +'ки' for i in input().split()]
#
# print(*c)

# --------------------


