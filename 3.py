#Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))

if 0 < x < float('inf') and 0 < y < float('inf'):
    print('1 четверть!')
elif 0 > x > float('-inf') and 0 < y < float('inf'):
    print('2 четверть!')
elif 0 > x > float('-inf') and 0 > y > float('-inf'):
    print('3 четверть!')
elif 0 < x < float('inf') and 0 > y > float('-inf'):
    print('4 четверть!')
elif x == 0 and  y == 0:
    print('Начало координат!')
