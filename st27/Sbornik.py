class Sbornik:
    def __init__(self):
        self.name = None
        self.developer = None
        self.date = None

    def create_sbornik(self):
        self.name = input("Наименование Сборника: ")
        self.developer = input("Разработчик Сборника: ")
        self.date = input("Дата согласования: ")

    def print_sbornik(self):
        print("Наименование Сборника: " + self.name)
        print("Разработчик Сборника: " + self.developer)
        print("Дата согласования: " + self.date)

    def change_sbornik(self):
        self.name = input("Новое наименование Сборника: ")
        self.developer = input("Новый разработчик сборника: ")
        self.date = input("Новая дата согласования: ")
