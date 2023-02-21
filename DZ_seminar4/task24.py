# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод.  В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите количество кустов N '))
lot_berry = [
    int(input(f'Введите количество ягод на {i} кусте ')) for i in range(1, n + 1)]
max_count_berry = 0
count_berry = 0
for i in range(n):
    if i == 0:
        count_berry = lot_berry[0] + lot_berry[1] + \
            lot_berry[len(lot_berry) - 1]
    elif i == len(lot_berry) - 1:
        count_berry = lot_berry[0] + \
            lot_berry[len(lot_berry) - 2] + lot_berry[len(lot_berry) - 1]
    else:
        count_berry = lot_berry[i - 1] + lot_berry[i] + lot_berry[i + 1]
    if max_count_berry < count_berry:
        max_count_berry = count_berry
        ind = i + 1
print(
    f'Максимальное количество ягод, которое может собрать за один заход собирающий модуль, равно {max_count_berry}.')
print(f'При этом он будет находиться перед кустом {ind}.')
