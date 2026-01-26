import math
from curses.ascii import isalnum
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


# nik = input()
#
# if nik[0] == '@' and 5 <= len(nik) <= 15 and nik[1:].isalnum() and (nik[1:].islower() or nik[1:].isdigit()):
#     print('Correct')
# else:
#     print('Incorrect')



# number = input()
#
# alpha = 'АВЕКМНОРСТУХ'
#
# if (number[0] in alpha
#     and number[1:4].isdigit()
#     and number[4] in alpha
#     and number[5] in alpha
#     and number[6] == '_'
#     and number[7:10].isdigit()
#     and 9 <= len(number) <= 10):
#
#     print('YES')
# else:
#     print('NO')

# day = input()
# euro = input()
# uan = input()
#
# s = f'На {day}: 1€ = {euro}₽, 1¥ = {uan}₽'
#
# print(s)

# a = int(input())
# b = int(input())
#
# print(f'Для чисел {a} и {b}:')
# print(f'    Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}')
# print(f'    Куб суммы: ({a} + {b})**3 = {(a + b)**3}')


# day = int(input())
# weight = float(input())
#
# correct_weight = 100 - (0.2 * day)
#
# if weight <= correct_weight:
#     print(f'Все идет по плану \n'
#           f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {correct_weight} кг')
#
# else:
#     print(f'Что-то пошло не так \n'
#           f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {correct_weight} кг')


# letter = ord(input())
#
# if letter == 1071:
#     print('Дальше букв нет')
# else:
#     print(chr(letter + 1))


# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     print(chr(i), end=' ')


# s = input()
#
# for i in s:
#     print(ord(i), end=' ')


# word = input()
# word1 = input()
# word2 = input()
# word3 = input()
# count = 0
# count1 = 0
# count2 = 0
# count3 = 0
#
# for i in range(len(word)):
#     count += ord(word[i])
#
# for j in range(len(word1)):
#     count1 += ord(word1[j])
#
# for h in range(len(word2)):
#     count2 += ord(word2[h])
#
# for n in range(len(word3)):
#     count3 += ord(word3[n])
#
# max_count = (max(count, count1, count2, count3))
#
# if max_count == count:
#     print(word)
# elif max_count == count1:
#     print(word1)
# elif max_count == count2:
#     print(word2)
# else:
#     print(word3)


# -------------------------------

# s = input()
# count = 0
#
# for i in s:
#     count += ord(i)
# print(f"Текст сообщения: '{s}'")
# print(f'Стоимость сообщения: {count * 3}🐝')


# -------------------------------

# s = input()
# count = 0
# count1 =0
# eng = 'eyopaxcETOPAHXCBM'
# rus = 'еуорахсЕТОРАНХСВМ'
#
# for i in s:
#     count += ord(i)
#
# for h in range(len(eng)):
#     s = s.replace(eng[h], rus[h])
# for g in s:
#     count1 += ord(g)
#
# print(f'Старая стоимость: {count * 3}')
# print(f'Новая стоимость: {count1 * 3}')

# ---------------------------------
# шифр Цезаря
# n = int(input())
# s = input()
#
# for i in s:
#     new = ord(i) - n
#     if new < 97:
#         new += 26
#     print(chr(new), end='')



# word = input()
# word1 = input()
# word2 = input()
# word3 = input()
#
# max_word = max(word, word1, word2, word3)
# min_word = min(word, word1, word2, word3)
#
# magic = (ord(max_word[-1]) * ord(min_word[-1])) ** 2
#
# print(magic)

# word = input()
# max_word = ''
# min_word = word
# while word != 'КОНЕЦ':
#     if min_word > word:
#         min_word = word
#     if max_word < word:
#         max_word = word
#
#     word = input()
#
# print('Минимальная строка ⬆️:', min_word)
# print('Максимальная строка ⬆️:', max_word)











