# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).


def enter(str):
    if str == 0:
        return ""
    res = input()
    return enter(str - 1) + f'{res} '

print(enter(int(input('Введите N: '))))
