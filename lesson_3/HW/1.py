# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

N = int(input("Введите число N: "))
A = []
number = 0
for i in range(N):
    A.append(random.randint(-N, N))

for i in A:
    print(i)

X=int(input('Введите число X: '))

for i in range(N):
    if A[i]==X:
        number+=1

print(f'X встречается {number} раз в массиве')
