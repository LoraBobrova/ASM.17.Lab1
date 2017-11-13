from .Worker import *

class Fired(Worker):
    def __init__ (self):
        super().__init__()
        self.type = 'Бывший сотрудник'
        self.date = ''
        self.reason = ''
        
    def Write(self):
        super().Write()
        self.date = input("Дата увольнения: ")
        self.reason = input("Причина увольнения: ")

    
    def __str__(self):
        return super().__str__() + 'Дата увольнения: {}\nПричина увольнения: {}'.format(self.date, self.reason)
