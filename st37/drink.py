from .food import *

class drink(food):
    pass

           
    def vvod(self):
        self.alcogol = input('Введите алкогольный ли напиток\n')
        super().vvod()
        

    def vyvod(self):
        print('Алкоголь? ' + self.alcogol)
        super().vyvod()
        
