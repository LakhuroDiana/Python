# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

array = list(map(int, input("введите списко: ").split()))
a=0

# for i in range(0, len(array)+1):
#     for j in range(i+1, len(array)):
#         if array[i]==array[j]:
#             a+=1

# print(a)

print(sum(array[i]==array[j] for i in range(0, len(array)+1) for j in range(i+1, len(array))))