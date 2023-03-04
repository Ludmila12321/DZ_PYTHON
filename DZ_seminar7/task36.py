# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        [print(operation(i, j), end=' ') for j in range(1, num_columns + 1)] 
        print()

summation = lambda x, y: x + y
difference = lambda x, y: x - y
multiplication = lambda x, y: x * y
fission = lambda x, y: round(x / y, 2)
print('Введите размер требуемой таблицы.')
num_rows = int(input('Количество строк:  '))
num_columns = int(input('Количество столбцов:  '))
print('Результаты какой бинарной операции вы хотите получить в таблице?')
print('Чтобы получить сумму, нажмите s')
print('Чтобы получить разность, нажмите d')
print('Чтобы получить произведение, нажмите m')
print('Чтобы получить результаты деления, нажмите f')
flag = input('Ваш выбор:  ')
print()
if flag == 's':
    print_operation_table(summation, num_rows, num_columns)
elif flag == 'd':
    print_operation_table(difference, num_rows, num_columns)
elif flag == 'm':
    print_operation_table(multiplication, num_rows, num_columns)
elif flag == 'f':
    print_operation_table(fission, num_rows, num_columns)   
else:
    print('Увы! Такой операции нет.')