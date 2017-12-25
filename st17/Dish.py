from st17.ListCommand import *

class Dish:

    def __init__(self):
        self.name=""
        self.price=0
        self.grams=0
        self.description=""
        self.edit=[self.AddName,self.AddPrice,self.AddGrams,self.AddDescription]
    
    def AddDish(self):
        self.AddName()
        self.AddPrice()
        self.AddGrams()
        self.AddDescription()

    def AddName(self):
        self.name=input("Enter name\n")
    
    def AddPrice(self):
        self.price=WhileTest(IsFloat,"Enter price\n")

    def AddGrams(self):
        self.grams=WhileTest(IsFloat,"Enter grams\n")

    def AddDescription(self):
        self.description=input("Enter description\n")

    def ShowDish(self):
        print("""
0) name - {0}
1) price - {1}
2) grams - {2}
3) description - {3}""".format(self.name,self.price,self.grams,self.description))

    def EditDish(self):
        while(True):
            self.ShowDish()
            i=WhileTest(IsInt,"\nEnter the parameter dish number for editing. To return enter -1.\n")
            if (int(i)==-1):
                break
            if ((int(i)>-1)and(int(i)<len(self.edit))):
                self.edit[int(i)]()
            else:
                print("\nEnter a number in the range from -1 to {0}".format(len(self.edit)-1))
            
