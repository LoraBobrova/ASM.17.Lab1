from .Category import *

class Dish(Category):
        def __init__(self):
                super().__init__()
                self.inp_dish()
            
        def inp_dish(self):
                self.num_id = int(input("Номер блюда: "))
                self.name = input("Название блюда: ")
                self.weight = input("Вес: ")
                self.price = input("Цена: ")

        def output(self):
                print("Категория:", self.tittle)
                print("Номер:", self.num_id)
                print("Название:", self.name)
                print("Вес:", self.weight)
                print("Цена:", self.price)

        

