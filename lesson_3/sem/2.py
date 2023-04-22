# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

import random
N=int(input('Введите размер последовательности: '))
K=int(input('Введите K: '))
A=[]
for i in range(N):
    A.append(random.randint(-N,N))

print(A)

for i in range(K):
    A.insert(0, A.pop())

print(A)