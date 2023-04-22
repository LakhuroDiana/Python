# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
N = int(input("Введите количество элементов в массиве: "))
list = []
for i in range(N):
    list.append(int(input()))
print(list)

# sum=0
# for i in range(1,N):
#     if list[i-1]>list[i]:
#         sum+=1
# print(sum)

res = [list[i] > list[i - 1] for i in range(1, N)]
print(sum(res))
