#  Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
n=int(input('Введите n: '))
m=int(input('Введите m: '))
first =[]
second = []
for i in range(n):
    first.append(random.randint(-n, n))
for i in range(m):
    second.append(random.randint(-m, m))
a=sorted((set(first)).intersection(set(second)))
print(a)