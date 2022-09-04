#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if quarter > 4 or quarter < 1:
    print('Вы ввели не допустимое значение!')
elif quarter == 1:
    print('0 < X < ♾ и 0 < Y < ♾')
elif quarter == 2:
    print('-♾ < X < 0 и 0 < Y < ♾')
elif quarter == 3:
    print('-♾ < X < 0 и -♾ < Y < 0')
elif quarter == 4:
    print('0 < X < ♾ и -♾ < Y < 0')

