# Даны три числа. Найти наименьшее из них.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a > b and a > c:
    print('Большее : ',a)
elif b > a and b > c:
    print('Большее : ',b)
else:
    print('Большее : ',c)