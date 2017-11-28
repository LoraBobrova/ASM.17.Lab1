from .student import *

class Mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
        self.doljnost = ""
    
    def read(self):
        super().read()
        self.telephone = input("Введите номер телефона: ")
        self.doljnost  = input("Введите должность: ")

    def write(self):
        super().write()
        print("Номер телефона: ", self.telephone)
        print("Должность: ", self.doljnost)
        
