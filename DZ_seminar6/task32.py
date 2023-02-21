# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def between_min_max(p_min, p_max, array):
    return [i for i in range(len(array)) if p_min < array[i] < p_max]
    
lst = [randint(-20, 20) for _ in range(10)]
preset_min = int(input('Задайте значение минимума '))
preset_max = int(input('Задайте значение максимума '))
print('Проверяемый массив', lst)

print('Индексы элементов массива, значения которых в заданном диапазоне', between_min_max(preset_min, preset_max, lst))