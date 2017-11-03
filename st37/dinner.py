from .drink import *
import pickle

class dinner:
    kartoteka = []
    f = 'st37/kartoteka.pkl'

    def __init__(self):
        pass
        

    def add_food(self):
        g = food()
        g.vvod()
        self.kartoteka.append(g)
        print("\nWell done\n")

    def add_drink(self):
        d = drink()
        d.vvod()
        self.kartoteka.append(d)
        print("\nХорошо\n")

    def all_(self):
        if len(self.kartoteka)==0:
            print('Элементов нет\n')
        else:
            for i in range(0,len(self.kartoteka)):
                print('\n')
                self.kartoteka[i].vyvod()
          

    def write(self):
        s = open(dinner.f,'wb')
        pickle.dump(self.kartoteka,s)
        s.close()
        print("\nЗапись прошла успешно\n")

    def read(self):
        r = open(dinner.f,'rb')
        self.kartoteka = pickle.load(r)
        r.close()
        print("\nФайл прочитан\n")

    def edit(self):
        try:
            j = input('Введите номер блюда для изменения\n')
            i = int(j)
            self.kartoteka[i].vvod()
            print("\nЭлемент изменен\n")
        except IndexError:
            print('Такого элемента в списке нет\n')

    def clear(self):
        self.kartoteka.clear()
        print("\nСписок очищен\n")
        
