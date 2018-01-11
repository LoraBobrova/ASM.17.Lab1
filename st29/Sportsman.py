class MyClass():
    def __init__(self, surname= ' ', name= ' ', age= ' ', height= ' ', weight= ' '):
        self.surname= surname
        self.name= name
        self.age= age
        self.height= height
        self.weight= weight
	
    def read_data(self):
        self.surname = input("Surname: ", )
        self.name = input("Name: ", )
        self.age = input("Age: ", )
        self.height = input("Height: ", )
        self.weight = input("Weight: ", )
	
    def write_data(self):
        print(self.surname, self.name, self.age, self.height, self.weight)
	        
