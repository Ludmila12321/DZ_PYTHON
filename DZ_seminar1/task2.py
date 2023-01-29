# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = input('Введите любое трёхзначное число: ')
if len(number) == 4 and number[0] == '-':
        print('Сумма цифр данного числа равна ', int(number[1]) + int(number[2]) + int(number[3])) # Минус не считаем, т. к. математически минус - не цифра
elif number[0] == '0' or len(number) != 3:
    print('Читайте внимательнее условие! Число должно быть трёхзначным!')
else:
    for i in range(len(number)):
        if number[i] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!"№;:*()_-=+/<>[]{&^$}#@~':
            print('Вы ввели не число!')
            break
    else:
        print('Сумма цифр данного числа равна ', int(number[0]) + int(number[1]) + int(number[2]))
