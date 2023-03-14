from data_creating import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    with open('database_phonebook.csv', 'a', encoding='utf-8') as file:
        file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    
def print_data():
    print('Выводим данные из телефонной книги\n')
    with open('database_phonebook.csv', 'r', encoding='utf-8') as file:
        data_phonebook = file.readlines()
        data_phonebook_version_second = []
        j = 0
        for i in range(len(data_phonebook)):
            if data_phonebook[i] == '\n' or i == len(data_phonebook) - 1:
                data_phonebook_version_second.append(''.join(data_phonebook[j:i + 1]))
                j = i
        data_phonebook = data_phonebook_version_second
        print(''.join(data_phonebook))
    return data_phonebook

def put_data():
    data_phonebook = print_data()
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    print(f'Изменить данную запись\n{data_phonebook[number_journal]}')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    data_phonebook = data_phonebook[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_phonebook[number_journal + 1:]
    with open('database_phonebook.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_phonebook))
    print('Изменения успешно сохранены!')
    
def delete_data():
    data_phonebook = print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    print(f'Удалить данную запись\n{data_phonebook[number_journal - 1]}')
    data_phonebook = data_phonebook[:number_journal] + data_phonebook[number_journal + 1:]
    with open('database_phonebook.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_phonebook))
    print('Изменения успешно сохранены!')