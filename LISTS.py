from itertools import count

n = input()
c = ''
numbers = list(n)

for i in range(len(numbers)):
    if i % 2 == 0:
        c += numbers[i]
print(list(c))


