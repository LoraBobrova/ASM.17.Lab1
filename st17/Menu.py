from st17.VipDish import VipDish
from st17.Dish import Dish
from st17.ListCommand import *
import pickle

class Menu:

    def __init__(self):
        self.listdish=[]

    def AddDishMenu(self):
        d=Dish()
        d.AddDish()
        self.listdish.append(d)

    def AddVipDishMenu(self):
        vd=VipDish()
        vd.AddVipDish()
        self.listdish.append(vd)

    def ShowDishMenu(self):
        if (len(self.listdish)>0):
            for i in self.listdish:
                print("")
                print("id -",self.listdish.index(i))
                i.ShowDish()
        else:
            print("The menu is empty")

    def ClearDishMenu(self):
        self.listdish.clear()
        print("Menu cleared.\n")

    def SafeDishMenu(self):
        if (len(self.listdish)>0):
            #nf=input("Enter the name of the file to save\n")
            with open("st17/menu.pkl","wb")as f:
                pickle.dump(self.listdish,f)
            print("File saved")
        else:
            print("The menu is empty")

    def LoadDishMenu(self):
        #nf=input("Enter the name of the file to upload\n")
        if (IsFile(nf)):
            with open("st17/menu.pkl","rb") as f:
                self.listdish=pickle.load(f)
            print("File downloaded")
            self.ShowDishMenu()
        else:
            print("This file does not exist")
        
    def EditDishMenu(self):
        if (len(self.listdish)>0):
            self.ShowDishMenu()
            p=""
            while(True):
                i=WhileTest(IsInt,p,"\nEnter the dish id for editing. To return enter -1.\n")
                if (int(i)==-1):
                    break
                if ((int(i)<len(self.listdish))and(int(i)>-1)):
                    self.listdish[int(i)].EditDish()
                    self.ShowDishMenu()
        else:
            print("The menu is empty")
            
