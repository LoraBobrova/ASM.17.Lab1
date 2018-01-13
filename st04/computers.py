import pickle, copy, os
from .computer_case import Computer_case
from .notebook import Notebook

class Computers:
    def __init__(self):
        self.l=list()
        
    def read(self):
        print("Enter the type of computer\n1.Computer_case\n2.Notebook")
        k = input()
        if (k=="1"):
            self.l.append(copy.deepcopy(Computer_case()))
        elif (k=="2"):
            self.l.append(copy.deepcopy(Notebook()))
        else:
            print("Incorrect value")
            return 0
        self.l[len(self.l)-1].read()
        return 1
        
    def write(self):
        i=1
        for o in self.l:
            print("PC", i)
            o.write()
            i+=1
            print("------------")
            
        if (len(self.l)==0):
            print("the list is empty")
            
            
    def change(self):
        self.write()
        if (len(self.l)!=0):
            print("Choose the number of PC")
            try:
                m = int(input())
                if (m>0) and (m<=len(self.l)):
                    if (self.read()==1):
                        self.l[m-1] = self.l[len(self.l)-1]
                        self.l.pop()
                        print("Change!")
                else:
                   print("Incorrect value")
            except:
                print("Incorrect value")

    def delete(self):
        self.write()
        if (len(self.l)!=0):
            print("Choose the number of PC")
            try:
                m = int(input())
                if (m>0) and (m<=len(self.l)):
                        self.l.pop(m-1)
                        print("Delete!")
                else:
                   print("Incorrect value")
            except:
                print("Incorrect value")
            
        
        
            
    def read_file(self):
        if (os.path.exists("st04/file.dat")):
            self.l = pickle.load(open("st04/file.dat", "rb"))
            print("Read list!")
        else:
            print("File not found!")
            

        
    def write_file(self):
            pickle.dump(self.l, open("st04/file.dat", "wb"))
            print("Write list!")

    def clear(self):
        self.l.clear()
        
    

    
