# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:  пара-ра-рам рам-пам-папам па-ра-па-дам  Вывод: Парам пам-пам

def checking_text(text):
    text = text.lower().split()
    for i in range(len(text)):
        counter = 0
        str_1 = text[i]
        for s in range(len(str_1)):
            if str_1[s] in 'аеёиоуыэюя':
                counter += 1
        if i == 0:
            counter_1 = counter
        elif counter_1 != counter:
            return 'Пам парам' 
    return 'Парам пам-пам'
   
check_text = input('Введите текст стихотворения: ')

print(checking_text(check_text))