from st17.Dish import Dish
from st17.VipDish import VipDish
from st17.ListCommand import *
import pickle

class Menu:

    def __init__(self):
        self.listdish=[]

    def AddDishInMenu(self):
        d=Dish()
        d.AddDish()
        self.listdish.append(d)

    def AddVipDishInMenu(self):
        vd=VipDish()
        vd.AddVipDish()
        self.listdish.append(vd)

    def ShowMenu(self):
        if (len(self.listdish)>0):
            for i in self.listdish:
                print("")
                print("id -",self.listdish.index(i))
                i.ShowDish()
        else:
            print("The menu is empty")

    def EditDishInMenu(self):
        if (len(self.listdish)>0):
            while(True):
                self.ShowMenu()
                i=WhileTest(IsInt,"\nEnter the dish id for editing. To return enter -1.\n")
                if (int(i)==-1):
                    break
                if ((int(i)>-1)and(int(i)<len(self.listdish))):
                    self.listdish[int(i)].EditDish()
                else:
                    print("\nEnter a number in the range from -1 to {0}".format(len(self.listdish)-1))
        else:
            print("The menu is empty")

    def SafeMenu(self):
        if (len(self.listdish)>0):
            nf=input("Enter the name of the file to save\n")
            with open("st17/"+nf,"wb")as f:
                pickle.dump(self.listdish,f)
            print("File saved")
        else:
            print("The menu is empty")

    def LoadMenu(self):
        nf=input("Enter the name of the file to upload\n")
        if (IsFile(nf)):
            with open("st17/"+nf,"rb") as f:
                self.listdish=pickle.load(f)
            print("File downloaded")
            self.ShowMenu()
        else:
            print("This file does not exist")

    def ClearMenu(self):
        self.listdish.clear()
        print("Menu cleared.\n")
            
