# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
import random

grades = list(map(int, input('введите оценки: ').split()))

#grades = list(map(int, a=random.randint(2, 5)))
# grades = list( random.randint(2, 5) for i in grades_1)
print(grades)


max_grade = max(grades)
min_grade = min(grades)

result = [i if i != max_grade else min_grade for i in grades]
print(result)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

