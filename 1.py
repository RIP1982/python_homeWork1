#Напишите программу, которая принимает на вход цифру,
#обозначающую день недели, и проверяет, является ли этот день выходным.
dayNumber = int(input('Введите число, соответствующее дню недели:\n '
                      'Monday = 1\n '
                      'Tuesday = 2\n '
                      'Wednesday = 3\n '
                      'Thursday = 4\n '
                      'Friday = 5\n '
                      'Saturday = 6\n'
                      ' Sunday = 7\n'))

if 6 <= dayNumber <= 7:
    print('Этот день выходной!')
elif 1 <= dayNumber <= 5:
    print('Этот день рабочий!')
elif dayNumber > 7 or dayNumber < 1:
    print('Вы ввели не допустимое значение!')


