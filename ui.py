from ast import Break
from logger import input_data, print_data, changing_data, deleting_data, search_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n1) Запись данных контакта. \n\
2) Вывод всех контактов. \n3) Изменение данных контакта.\n4) Удаление данных контакта. \n5) Поиск контакта. \n\
6) Выйти из справочника")
    command = int(input('Введите число в соответствии с выбранной командой: '))

    while command != 1 and command != 2 and command != 3 and command != 4 and command != 5 and command != 6:
        print("Некорректный ввод!")
        comand = int(input('Введите число в соответствии с выбранной командой: '))

    if command == 1:
        input_data()
        interface()
    elif command == 2:
        print_data()
        interface()
    elif command == 3:
        changing_data()
        interface()
    elif command == 4:
        deleting_data()
        interface()
    elif command == 5:
        search_data()
        interface()
    elif command == 6:
        Break

interface()



