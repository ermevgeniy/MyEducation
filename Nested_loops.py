import math
from ipaddress import summarize_address_range
from itertools import count

# n = int(input())
# counter = 0
#
# for i in range(1, n +1):
#     fak = math.factorial(i)
# print(fak)


#
# num = int(input())
#
# while num % 7 == 0:
#     print(num)
#     num = int(input())


# price = int(input())
# count = 0
# while price >= 25:
#     price -= 25
#     count += 1
# while price >= 10:
#     price -= 10
#     count += 1
# while price >= 5:
#     price -= 5
#     count += 1
# while price >= 1:
#     price -= 1
#     count += 1
# print(count)



# num = int(input())
# count = 0
# count1 = 9
# while num != 0:
#     last = num % 10
#     if last > count:
#         count = last
#
#     if last < count1 :
#         count1 = last
#     num = num // 10
#
# print("Максимальная цифра равна", count)
# print("Минимальная цифра равна", count1)

# num = int(input())
# sum1 = 0
# count = 0
# multi = 1
# average = 0
# first = 0
# copy = num % 10
#
# while num > 0:
#     last_digit = num % 10
#     sum1 += last_digit
#     count +=1
#     multi *= last_digit
#     average = sum1 / count
#     first_digit = num
#     sum2 = copy + first_digit
#
#     num //= 10
#
# print(sum1)
# print(count)
# print(multi)
# print(average)
# print(first_digit)
# print(sum2)




# n = int(input())
# count = n % 10
# flag = True
#
# while n > 0:
#     digit = n % 10
#     if digit != count:
#         flag = False
#     n //= 10
#
# if flag == True:
#     print("YES")
# else:
#     print("NO")

#
# num = int(input())
# count = 0
# n = len(str(num))
#
# for i in range(1, n + 1):
#     digit = num // 10 ** (n - i) % 10
#     if digit % 2 == 0:
#         count += 1
#         print(count,'-я', ' четная цифра равна ', digit, sep='')
#
# if count == 0:
#     print("Четных цифр в числе нет")



# n = int(input())
#
# last_num = 0
#
# flag = True
#
# while n > 0:
#     digit = n % 10
#     if last_num > digit:
#         flag = False
#
#     last_num = digit
#     n //= 10
#
# if flag == True:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)

# n = int(input())
# while n > 0:
#     digit = n % 10
#     n //= 10
#
# print(digit)

# count = 0
# multi = 1
# for _ in range(10):
#     x = int(input())
#     if x >= 0:
#         multi *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(multi)
# else:
#     print('NO')

# Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3. Если в числе нет цифр, кратных 3, требуется на экран вывести «NO»
# n = int(input())
# max_digit = -1
#
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#
#         if max_digit < digit:
#             max_digit = digit
#     n //= 10
#
# if max_digit == -1:
#      print('NO')
# else:
#      print(max_digit)

#
# mx = -1000000
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if mx < x < 0:
#         mx = x
#
# if s != 0:
#     print(s)
#
# if mx != -1000000:
#     print(mx)
#
# else:
#     print("NO")

# ******
# ******
# ******
# ******
# ******
# ******
# ******
# ******
#
# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()



# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
#
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


# n = int(input())
#
# for i in range(1, n//2 + 2):
#         print("*" * i)









# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#
#     print()
#
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# 28n + 30k + 31m = 365

# 13    12    11

# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 13):
#            if  28 * n + 30 * k + 31 * m == 365:
#             print(n, k, m)


# 10x + 5y + 0.5z = 100

#10    20    200
#
# for x in range(1, 11):
#     for y in range(1, 21):
#         for z in range(1, 201):
#             if 10 * x + 5 * y + 0.5 * z == 100:
#                 if x + y + z == 100:
#                     print(x, y, z)




# a + b + c + d = 150

#38

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 < e ** 5:
#                         break
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a + b + c + d + e)


# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j , end='')
#     for h in range(i - 1, 0, -1):
#         print(h, end='')
#     print()


# while True:
#     num1 = int(input())
#     num2 = int(input())
#     print("Сумма чисел:", num1 + num2)
#     string = input("Нажмите Y или y для завершения программы:")
#
#     if string == 'Y' or string == 'y':
#         break

#
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов +,
# сколько делителей у этого числа.
# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(i, i + 1):
#         for h in range(1, j + 1):
#             if j % h == 0:
#                 print("+", end='')
#     print()


# a = int(input())
# b = int(input())
#
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count +=1
#
#     if count == 2:
#         print(i)

# n = int(input())
# count = 1
# summa = 0
# for i in range(1, n + 1):
#     count *= i
#     summa += count
#
# print(summa)


# n = int(input())
# m = int(input())
# flag = False
#
# for i in range(1, n):
#     for j in range(1, n):
#         for g in range(1, n):
#             if i + 3 * j + 2 * g == m:
#                 print(f'{i} + 3×{j} + 2×{g} = {m}')
#
#                 flag = True
#
# if flag == False:
#     print("При заданных n и m решений не существует.")

# ----------------ДЕЛИТЕЛИ-----------
# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(i, i + 1):
#         for h in range(1, j + 1):
#             if j % h == 0:
#                 print("+", end='')
#     print()
#
#
# a = int(input())
# b = int(input())
# number = 0
# max_count = 0
# max_sum = 0
# for i in range(a, b + 1):
#     summa = 0
#     for j in range(1, i + 1):
#             if i % j == 0:
#                 summa += j
#     if summa > max_sum or (summa == max_sum and i > number):
#         max_sum = summa
#         number = i
# print(number, max_sum)


# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         total += 1
#         print(total, end=' ')
#     print()

# ЧИСЛЕННЫЙ ТРЕУГОЛЬНИК
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for h in range(i -1, 0, -1):
#         print(h, end='')
#
#     print()

# n = int(input())
# count = 0
# while n > 0:
#     num = n // 1 % 10
#     n //= 10
#     count += num
#     while count >= 10:
#         num1 = count // 1 % 10
#         count //= 10
#         count += num1
# print(count)

#
# n = 8
# count = 0
# maximum = -1000
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4
# count = 0
# maximum = -10 ** 8
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
#
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
#
# for i in range(n):
#     if i !=0 and i != n - 1:
#         print('*                 *')
#     else:
#         print(19 * '*')
#


# n = int(input())
#
# while n > 99:
#     num = n // 1 % 10
#     n //= 10
#
# print(num)


# n = int(input())
# count_last = n // 1 % 10
# count = 0
# countLast = 0
# counter = 0
# summa_num = 0
# a = 1
# b = 0
# while n > 0:
#     num = n // 1 % 10
#
#     if num == 3:
#         count += 1
#     if num == count_last:
#         countLast +=1
#     if num % 2 == 0:
#         counter +=1
#     if num > 5:
#         summa_num += num
#     if num > 7:
#         a *= num
#     if num == 0 or num == 5:
#         b += 1
#
#     n //= 10
#
# print(count)
# print(countLast)
# print(counter)
# print(summa_num)
# print(a)
# print(b)


# n = int(input())
# s = 0
# f = 0
# for a in range(1, n + 1):
#     for b in range(a, n + 1):
#         summa = a ** 3 + b ** 3
#         if summa != s:
#             s = summa









