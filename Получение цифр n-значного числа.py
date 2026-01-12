#Формула для вычисления i-й цифры n-значного числа num в общем виде:

num = 956555


c = num // 1000 % 10 # 4я с конца
print(c)

# для чайников:

# 123456789 // 1 % 10 ---> 9 (единицы)

# 123456789 // 10 % 10 ---> 8 (десятки)

# 123456789 // 100 % 10 ---> 7 (сотни)

# 123456789 // 1000 % 10 ---> 6 (тысячи)

# 123456789 // 10000 % 10 ---> 5 (десятки тысяч)

# 123456789 // 100000 % 10 ---> 4 (сотни тысяч)

# 123456789 // 1000000 % 10 ---> 3 (миллионы)

# 123456789 // 10000000 % 10 ---> 2 (десятки миллионов)

# 123456789 // 100000000 % 10 ---> 1 (сотни миллионов)



# АРИФМЕТИЧЕСКАЯ ПРОГРЕССИЯ
# (2b-c-a)(2c-b-a)(2a-b-c) == 0



# num = int(input())
#
# one_dig = num // 1 % 10
# two_dig = num // 10 % 10
# three_dig = num // 100 % 10
#
# sum = one_dig + two_dig + three_dig
# mult = one_dig * two_dig * three_dig
#
# print("Сумма цифр = ", sum, '\n' "Произведение цифр = ", mult, sep="")


# num = int(input())
#
# first_digit = num // 1 % 10
# second_digit = num // 10 % 10
# third_digit = num // 100 % 10
# fourth_digit = num // 1000 % 10
#
#
# a = num % 10000 // 1000

# print(100 * first_digit + 10 * average_digit + last_digit)
# print(100 * first_digit + 10 * last_digit + average_digit)
# print(100 * average_digit + 10 * first_digit + last_digit)
# print(100 * average_digit + 10 * last_digit + first_digit)
# print(100 * last_digit + 10 * first_digit + average_digit)
# print(100 * last_digit + 10 * average_digit + first_digit)