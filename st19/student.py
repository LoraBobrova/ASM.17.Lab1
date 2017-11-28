class Student:
    def __init__(self):
        self.name = None
        self.sex = None
        self.age = None
        self.grants = None      
        
    def read(self):
        self.name = input("Введите имя: ")
        self.sex = input("Введите пол: ")
        self.age = input("Введите возраст: ")
        self.grants = input("Введите размер зарплаты: ")
        
    def write(self):
        print("Имя: ", self.name)
        print("Пол: ", self.sex)
        print("Возраст: ", self.age)
        print("Размер зарплаты: ", self.grants)
