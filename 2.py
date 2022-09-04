#Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Введите число X: '))
y = int(input('Введите число Y: '))
z = int(input('Введите число Z: '))

leftSide = not(x or y or z)
rightSide = not(x) and not(y) and not(z)

if leftSide == rightSide:
    print('true')
else:
    print('false')