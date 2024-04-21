from ast import Break
from copy import copy
from itertools import count
from shlex import join
from shutil import copyfile
from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name} | {surname} | {phone} | {address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n\n"
    f"Выберите вариант записи: "))
        
    while var != 1 and var != 2:
        print("Неправильный ввод!")
        var = int(input('Введите число: '))

    if var == 1:
        with open(file_1, 'a', encoding = 'utf-8') as f: 
            f.write(f"{name} | {surname} | {phone} | {address} \n\n")
    elif var == 2:
            with open(file_2, 'a', encoding = 'utf-8') as f:
                f.write(f"{name}; {surname}; {phone}; {address} \n\n") 

def print_data():
    var = int(input('Выберите  файл который желаете открыть для просмотра: \n'
    f'1) {file_1} \n'
    f'2) {file_2} \n'
    f'3) Оба файла\n'
    f'Введите № команды: '))

    while var != 1 and var != 2 and var != 3:
        print("Некорректный ввод!")
        var = int(input('Введите № команды: '))

    if var == 1 or var == 3:
        print('Вывожу данные из 1 файла:\n')
        with open(file_1, 'r', encoding = 'utf-8') as f:
            data_1 = f.readlines()
            print(*data_1)

    if var == 2 or var == 3:    
        print('Вывожу данные из 2 файла:\n')
        with open(file_2, 'r', encoding = 'utf-8') as f:
            data_2 = f.readlines()
            print(*data_2)

# def copy_file():
#     with open(file_1, 'r', encoding = 'utf-8') as f:
#         list_copy1 = []
#         for i in f:
#             list_copy1.append(i)
#     with open(file_2, 'r', encoding = 'utf-8') as f:
#         list_copy2 = []
#         for i in f:
#             list_copy2.append(i)    
#     return list_copy1, list_copy2

def changing_data():
    search_data()
    chang_data = input('Скопируйте в консоль контакт который желаете редактировать : \n')
    with open(file_1, 'r', encoding='utf-8') as f:
        list_copy1 = f.readlines()
    with open(file_2, 'r', encoding='utf-8') as f:
        list_copy2 = f.readlines()
    
    with open(file_1, 'w', encoding='utf-8') as f:
        for i in list_copy1:
            if chang_data in i:
                name = name_data()
                surname = surname_data()
                phone = phone_data()
                address = address_data()
                f.write(f'{name} | {surname} | {phone} | {address}\n')
            if chang_data not in i:
                f.write(i)

    with open(file_2, 'w', encoding='utf-8') as f:
        for i in list_copy2:
            if chang_data in i:
                name = name_data()
                surname = surname_data()
                phone = phone_data()
                address = address_data()
                f.write(f'{name}; {surname}; {phone}; {address}\n')
            if chang_data not in i:
                f.write(i)

    print(f'\n Изменения в контакте произведены...')
    

def deleting_data():
    search_data()  
    del_info = input('Скопируйте в консоль контакт который желаете удалить: \n')
    with open(file_1, 'r', encoding='utf-8') as f:
        list_copy1 = f.readlines()
    with open(file_2, 'r', encoding='utf-8') as f:
        list_copy2 = f.readlines()
    
    with open(file_1, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(list_copy1):  # Чтобы не выйти за пределы списка, -1
            if del_info in list_copy1[i]:
                i += 2  # Пропускаем искомую строку и следующую за ней строку
            else:
                f.write(list_copy1[i])
                i += 1
    
    with open(file_2, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(list_copy2):  # Чтобы не выйти за пределы списка, -1
            if del_info in list_copy2[i]:
                i += 2  # Пропускаем искомую строку и следующую за ней строку
            else:
                f.write(list_copy2[i])
                i += 1
    
    print('Выбранный контакт удален.')

def search_data():
    print('Выберите  файл в котором желаете осуществить поиск контакта: \n'
    f'1) {file_1} \n'
    f'2) {file_2}\n'
    f'3) Оба файла') 
    var = int(input('Введите № команды: '))
    while var != 1 and var != 2 and var != 3:
        print("Некорректный ввод!")
        var = int(input('Введите № команды: '))
    get_info = input('Введите данные для поиска: \n') 
    if var == 1 or var == 3:           
        with open(file_1, 'r', encoding = 'utf-8') as f:
            count1 = 0
            for i in f:
                words = i.strip().split(' | ')
                for word in words:
                    if word.lower() == get_info.lower():
                        count1+=1
                        print(f'Совпадение по поиску в файле {file_1}:\n {i}\n')
        
    if var == 2 or var == 3:
        with open(file_2, 'r', encoding = 'utf-8') as f:
            count2 = 0
            for j in f:
                words = j.strip().split('; ')
                for word in words:
                    if word.lower() == get_info.lower():
                        count2+=1
                        print(f'Совпадение по поиску в файле {file_2}:\n {j}\n')
        
    if count1 == 0 and count2 == 0:
        print(f'По вашему поиску нет данных.')
        var = int(input(f"Выберите команду\n\n"
        f"1) Желаете редактировать запрос \n"
        f"2) Главное меню \n"
        f"3) Выйти их программы \n"
        f"Введите № команды:  "))
        while var != 1 and var != 2 and var != 3:
            print("Некорректный ввод!")
            var = int(input('Введите № команды: '))
        if var == 1:
            search_data()
        elif var == 2:
            pass
        elif var == 3:
            Break

file_1 = 'data_1_var.csv'
file_2 = 'data_2_var.csv'