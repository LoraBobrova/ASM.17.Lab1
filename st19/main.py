from .group import *

group = University()

menu = {"1": ("Добавить студента", group.add_person),
        "2": ("Добавить преподавателя", group.add_new_person),
        "3": ("Редактировать", group.edit),
        "4": ("Удалить", group.delete),
        "5": ("Вывести список на экран", group.display_spisok),
        "6": ("Сохранить список в файл", group.napisat),
        "7": ("Загрузить список из файла", group.chtenie),
        "8": ("Очистить список", group.clean_out),
        "9": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 9:
            break
        menu[user_input][1]()
