# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

N=int(input('Введите размер списка: '))
list =[]
for i in range(N):
    n=int(input())
    list.append(n)
print (list)

print(len(set(list)))