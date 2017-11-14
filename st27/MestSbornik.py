from .Sbornik import Sbornik


class MestSbornik(Sbornik):
    def __init__(self):
        super().__init__()
        self.organization = None

    def create_sbornik(self):
        super().create_sbornik()
        self.organization = input("Организация для которой разработан Сборник: ")

    def print_sbornik(self):
        super().print_sbornik()
        print("Организация для которой разработан Сборник: " + self.organization)

    def change_sbornik(self):
        super().change_sbornik()
        self.organization = input("Новое наименование организации: ")
