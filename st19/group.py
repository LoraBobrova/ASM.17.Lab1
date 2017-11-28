from .mayor import *
import pickle

class University:
    Gubkin = "st19/file.pkl"
    spisok = []

    def __init__(self):
        pass

    def add_person(self):
        person = Student()
        person.read()
        self.spisok.append(person)
        print ("Студент добавлен")

    def add_new_person(self):
        new_person = Mayor()
        new_person.read()
        self.spisok.append(new_person)
        print ("Добавлен преподаватель")

    def display_spisok(self):
        if len(self.spisok)==0:
            print ("Список пуст\n")
        else:
            for i in range(0,len(self.spisok)):
                self.spisok[i].write()
                print ("\n")

    def chtenie(self):
        ponimanie = open(University.Gubkin,"rb")
        self.spisok = pickle.load(ponimanie)
        print ("Прочитано")

    def napisat(self):
        pismo = open(University.Gubkin,"wb")
        pickle.dump(self.spisok,pismo)
        pismo.close()
        print("Засчитано")

    def clean_out(self):
        self.spisok.clear()
        print ("Очищено")

    def edit(self):
        a = input("Запишите номер студента для редактирования: ")
        print("Запишите нового студента")
        self.spisok[int(a)].read()
        print("Редактировано")

    def delete(self):
        i = input("Запишите номер студента для удаления: ")
        self.spisok.pop(int(i))
        print("Удалено")
