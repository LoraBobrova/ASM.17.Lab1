import pickle 
from .Worker import *
from .Fired import *

class Company:
    def __init__(self):
        self.company = []
        
    def Add_Worker(self):
        worker = Worker()
        worker.Write()
        self.company.append(worker)

    def Add_Fired(self):
        worker = Fired()
        worker.Write()
        self.company.append(worker)
        
    def Show_List(self):
        if len(self.company) == 0:
            print("Список пуст")
        else:
            i = 0
            print ("Список работников:")
            for x in self.company:
                print(i,x)
                i += 1
            
    def Clear_List(self):
        self.company.clear()
        print ("Список очищен")

    def Write_File(self):
        pickle.dump(self.company, open('st06/file.dat', 'wb'))
        print ("Запись в файл выполнена")

    def Read_File(self):
        self.company = pickle.load(open('st06/file.dat', 'rb'))
        print ("Чтение из файла выполнено")

    def Edit_Worker(self):
        if len(self.company)==0:
            print("Список пуст")
            return
        n = int(input("Введите номер работника:"))
        if n <= (len(self.company)-1) and n >= 0:
            self.company[n].Write()
        else:
            print ("Некорректный ввод")
            return
            
    def Delete_Worker(self):
        if len(self.company) == 0:
            print("Список пуст")
            return
        n=int(input("Введите номер работника:"))
        if n <= (len(self.company)-1) and n >= 0:
            self.company.pop(n)
            print("Удаление выполнено") 
        else:
            print ("Некорректный ввод")
            return
