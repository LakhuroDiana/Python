# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно 
# ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

quantity=int(input('введите количество элементов: '))
difference=int(input('введите разность: '))
first_element=int(input('введите первый элемент: '))
list = [i for i in range(first_element, first_element+difference*(quantity-1)+1, difference)]
print(list)