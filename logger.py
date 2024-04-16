from ast import Break
from itertools import count
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
        with open('Sem_8/data_1_var.csv', 'a', encoding = 'utf-8') as f:
        
            f.write(f"{name} | {surname} | {phone} | {address}\n\n")
    elif var == 2:
            with open('Sem_8/data_2_var.csv', 'a', encoding = 'utf-8') as f:
                f.write(f"{name}; {surname}; {phone}; {address}\n\n") 

def print_data():
    print('Вывожу данные из 1 файла:\n')
    with open('Sem_8/data_1_var.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        print(*data_first)
        
    print('Вывожу данные из 2 файла:\n')
    with open('Sem_8/data_2_var.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def changing_data():
    search_data()
    print('Вы хотите изменить данные контакта {j}?')
    

def deleting_data():
    search_data()


def search_data():
    count1 = 0
    count2 = 0 
    get_info = input('Введите данные для поиска: \n')
     
    with open('Sem_8/data_1_var.csv', 'r', encoding = 'utf-8') as f:
        i = f.readlines()
        for i in f:
            words = i.split('|')
            for word in words:
                if word.lower() == get_info.lower():
                    count1+=1
                    print(f'По поиску в файле "data_1_var": \nСовпадение {count1}:\n {i}')
        
    
    with open('Sem_8/data_2_var.csv', 'r', encoding = 'utf-8') as f:
        j = f.readlines()
        for j in f:
            words = j.split(';')
            for word in words:
                if word.lower() == get_info.lower():
                    count2+=1
                    print(f'По поиску в файле "data_2_var": \nСовпадение {count2}:\n {j}')
        
    if count1 == 0 and count2 == 0:
        print(f'По вашему поиску нет данных.')
        var = int(input(f"Выберите команду\n"
        f"1) Желаете редактировать запрос \n"
        f"2) Главное меню \n"
        f"3) Выйти их программы \n"
        f"Введите число в соответствии с выбранной командой:  "))

        if var == 1:
            search_data()
        elif var == 2:
            pass
        elif var == 3:
            Break