6# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s=int(input('введите сколько журавликов они сделали вместе: '))
if s>=6 and s%6==0:
    K=int(4/6*s)
    P=int(1/6*s)
    S=int(1/6*s)
    print('Катя сделала {} самолётиков. Петя сделал {} самолётиков. Серёжа сделал {} самолётиков.'.format(K,P,S))
else:
    print('Самолётики целые!')
