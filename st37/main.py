from .dinner import *
dinner = dinner()

menu = {"1": ("Добавить блюдо", dinner.add_food),
        "2": ("Добавить напиток", dinner.add_drink),
        "3": ("Редактировать", dinner.edit),
        "4": ("Вывести список на экран", dinner.all_),
        "5": ("Сохранить список в файл", dinner.write),
        "6": ("Загрузить список из файла", dinner.read),
        "7": ("Очистить список", dinner.clear),
        "8": ("Выход", "")}

def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
            
        user_input = input("")
        if int(user_input) == 8:
            break
        menu[user_input][1]()
