from st17.ListCommand import *
from st17.Menu import Menu

def main():
    m=Menu()
    l=[m.AddDishInMenu,m.AddVipDishInMenu,m.EditDishInMenu,m.ClearMenu,m.ShowMenu,m.SafeMenu,m.LoadMenu]
    while (True):
        i=int(ShowList())
        if ((i>len(l)) or (i<0)):
            break
        MenuFunction(l[i])

if __name__ == "__main__":
    main()
