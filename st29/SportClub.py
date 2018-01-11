from .Sportsman import MyClass
from .Champion import SecondClass
import pickle

class SportClub:
    def __init__(self):
        self.club=[]

    def insertSportsman(self):
            newSportsman = MyClass()
            newSportsman.read_data()
            self.club.append(newSportsman)
            print('Sportsman added!')
            
    def insertChampion(self):
            newChampion = SecondClass()
            newChampion.read_data()
            self.club.append(newChampion)
            print('Champion added!')

    def showSportClub(self):
        for (i,club) in enumerate (self.club):
            print('Sportsman number',i+1)
            club.write_data()

    def edit(self):
        self.showSportClub()
        print('Enter the number element for edited')
        i=int(input())
        self.club[i-1].read_data()
        print('Number', i ,'was edited')
            

    def delete(self):
        self.showSportClub()
        print('Enter the number element for deleted')
        i=int(input())
        self.club.pop(i-1)
        print('Number', i ,'was deleted')

    def write_file(self):
        f=open('club.dat','wb')
        pickle.dump(self.club,f)
        print('Success!')
        
    def read_file(self):
        f=open('club.dat','rb')
        self.club = pickle.load(f)
        print('Success!')

    def clean(self):
        self.club.clear()
        print('Club is empty!')


