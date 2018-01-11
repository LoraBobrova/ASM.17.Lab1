from .Sportsman import MyClass

class SecondClass(MyClass):
    def __init__(self, surname = ' ', name= ' ', age= ' ', height= ' ', weight= ' ',competition= ' '):
        self.competition = competition;
        MyClass.__init__(self, surname, name, age, height, weight)
    
    def read_data(self):
        MyClass.read_data(self)
        self.competition = input("Competition: ", )

    def write_data(self):
        print(self.surname, self.name, self.age, self.height, self.weight,self.competition)
