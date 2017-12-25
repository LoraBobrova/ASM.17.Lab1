from st17.ListCommand import *
from st17.Dish import Dish

class VipDish(Dish):
    
    def __init__(self):
        Dish.__init__(self)
        self.bonus=0
        self.calories=0
        self.edit.extend([self.AddBonus,self.AddCalories])

    def AddVipDish(self):
        Dish.AddDish(self)
        self.AddBonus()
        self.AddCalories()

    def AddBonus(self):
        self.bonus=WhileTest(IsInt,"Enter bonus\n")

    def AddCalories(self):
        self.calories=WhileTest(IsFloat,"Enter calories\n")

    def ShowDish(self):
        Dish.ShowDish(self)
        print("""4) bonus - {0}
5) calories - {1}""".format(self.bonus,self.calories))


