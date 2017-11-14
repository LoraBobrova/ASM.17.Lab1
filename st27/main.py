from .eLibrary import eLibrary

library = eLibrary()

menu = {
    "1": (". Добавить новый Сборник", library.add_sbornik),
    "2": (". Добавить новый местный Сборник", library.add_mest_sbornik),
    "3": (". Удалить Сборник из электронной библиотеки", library.delete_sbornik),
    "4": (". Редактировать данные Сборника", library.change_elibrary),
    "5": (". Вывести электронную библиотеку на экран", library.print_elibrary),
    "6": (". Записать электронную библиотеку в файл", library.write_to_file),
    "7": (". Считать электронную библиотеку из файла", library.read_from_file),
    "8": (". Очистить электронную библиотеку", library.clear_elibrary),
    "9": (". Выйти", None)
}


def main():
    while True:
        print("Меню электронной библиотеки Сборников Газпрома:")
        for i in menu:
            print(i + menu[i][0])
        try:
            number = input("Введите команду: ")
            if number == "9":
                break
            else:
                menu[number][1]()

        except Exception as ex:
            print("Ошибка: такой команды не существует", ex)


if __name__ == "__main__":
    main()
