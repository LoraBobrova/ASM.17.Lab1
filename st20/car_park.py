import pickle
from st20.car import car
from st20.truck import truck
from st20.modul_show_run import *

class car_park:

    def __init__(self):
        self.park=[]

    def add_car(self):
        c=car()
        c.add()
        self.park.append(c)

    def add_truck(self):
        t=truck()
        t.add()
        self.park.append(t)

    def edit(self):
        if (len(self.park)>0):
            self.show()
            while(True):
                inp=input("Enter id for editing. To return to the menu enter 'back'.\n")
                if (str(inp)=="back"):
                    break
                if ((is_int(inp))and(int(inp)<len(self.park))and(int(inp)>-1)):
                    self.park[int(inp)].edit_car()
                    self.show()
        else:
            print("The car park is empty")

    def clear(self):
        self.park.clear()

    def show(self):
        if (len(self.park)>0):
            for i in self.park:
                print("")
                print("id -",self.park.index(i))
                i.show_car()
        else:
            print("The car park is empty")

    def safe(self):
        if (len(self.park)>0):
            inpf=input("Enter the name of the file to save\n")
            with open("st20/"+inpf,"wb")as f:
                pickle.dump(self.park,f)
            print("File successfully saved")
        else:
            print("The car park is empty")

    def load(self):
        outf=input("Enter the name of the file to upload\n")
        if (is_file(outf)):
            with open("st20/"+outf,"rb") as f:
                self.park=pickle.load(f)
            print("File uploaded successfully")
            self.show()
        else:
            print("This file does not exist")
