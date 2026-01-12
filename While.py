

# nik = input()
#
# line = "_"
#
# while line in nik:
#     nik = input()
#
# print(nik)


# name = input()
#
# count = -1
#
# flag = False
#
# while name != "Левон":
#
#     if name == "Александра":
#         flag = True
#
#     if flag == True:
#         count += 1
#
#     name = input()
#
# print(count)


# name = input()
#
# counter = 0
# while name != 'Левон':
#     counter += 1
#     if name == 'Александра':
#         counter = 0
#     name = input()
# print(counter)


num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag:  # эквивалентно if flag == True:
    print('Число простое')
else:
    print('Число составное')















