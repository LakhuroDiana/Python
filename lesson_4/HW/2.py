#  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
import random
k = int(input("введите количество кустов: "))
list=[]
for i in range(k):
    list.append(int(random.randint(1,10)))
print(list)
max=list[0]+list[1]+list[-1]
list.insert(0,list[k-1])
list.insert(k+1,list[1])
max=list[0]+list[1]+list[2]
for i in range(2,k-1):
    if list[i-1]+list[i]+list[i+2]>max:
        max=list[i-1]+list[i]+list[i+2]
print(max)


