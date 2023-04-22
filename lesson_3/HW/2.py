# Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

import random

N = int(input("Введите число N: "))
A = []
for i in range(N):
    A.append(random.randint(-N, N))

for i in A:
    print(i)

X=int(input('Введите число X: '))

difference = abs(A[0]-X)
number=A[0]
for i in range(N):
    if abs(A[i]-X)<difference:
        number=A[i]
        difference=abs(A[i]-X)

print(number)


