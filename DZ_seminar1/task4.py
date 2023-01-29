# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

number = int(input('Введите общее кол-во журавликов: '))
if number % 6 != 0:
    print(f'Увы, число {number} не подходит!')
else:
    print(f'Мальчики сделали по {number//6} журавликов. А Катя сделала {4*(number//6)} журавликов')