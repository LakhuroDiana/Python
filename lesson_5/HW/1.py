def pow_recursive(value, power):
    if power < 0:
        if value == 0:
            print("ERROR")
            return -1
        else:
            return 1 / (value * pow_recursive(value, -power - 1))
    if power == 0:
        if value == 0:
            print("uncertainty")
            return 0
        if value > 0:
            return 1
        if value < 0:
            return -1
    if power > 0:
        return value * pow_recursive(value, power - 1)

A=int(input('Введите A: '))
B=int(input('Введите B: '))

print(pow_recursive(A, B))
