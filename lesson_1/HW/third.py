# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

s=int(input('введите номер своего билетика: '))
a=0 #сумма первых 3 цифер
b=0 #сумма последних 3 цифер
while s>0:
    while s>1000:
        a+=s%10
        s//=10
    else:
        b+=s%10
        s//=10
if a==b:
    print('-> YES')
else:
    print('-> NO')
        