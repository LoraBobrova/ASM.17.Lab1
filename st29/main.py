from .SportClub import SportClub 

club=SportClub()
menu = {"1":("Add sport", club.insertSportsman),
        "2":("Add Champion", club.insertChampion),
        "3":("Edit", club.edit),
	"4":("Delete", club.delete),
	"5":("Show club", club.showSportClub),
	"6":("Read club from file", club.read_file),
	"7":("Write club to file", club.write_file),
	"8":("Clear", club.clean),
	"9":("Exit", None)}
def main():
    while True:
        print('')
        print('Menu:')
        for k in range(1,10):
            print(k,"-",menu[str(k)][0])
        x = input()
        if int(x)==9:
            break
        if int(x)>=1 and int(x)<9:
            menu[x][1]()
        else:
            print('Error! Choose other number')

if __name__ == "__main__":
    main()
	    
