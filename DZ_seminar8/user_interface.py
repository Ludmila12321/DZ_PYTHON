from logger import input_data, print_data, put_data, delete_data


def interface():
    print('Здравствуйте! Вы попали в телефонный справочник. Доступны следующие операции\n'
          '1. Записать контакт(ы) в телефонную книгу\n'
          '2. Удалить контакт(ы)\n'
          '3. Изменить контакт(ы)\n'
          '4. Вывести контакт(ы)\n')
    command = int(input("Введите номер нужной операции: "))

    while command < 1 or command > 4:
        print('К сожалению, такой операции нет')
        command = int(input("Введите номер нужной операции: "))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        put_data()
    else:
        print_data()