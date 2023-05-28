# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list = list(map(int, input('Введите список: ').split()))
min = int(input('введите минимум: '))
max = int(input('Введите максимум: '))

list_index=[i for i in range(0, len(list)) if min<=list[i]<=max]

# list_index=[]
# for i in range(0, len(list)):
#     if min<=list[i]<=max:
#         list_index.append(i)

print(list_index)
