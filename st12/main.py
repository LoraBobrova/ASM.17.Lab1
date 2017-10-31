from .classContainerFIle import classContainer
#from .descendantClassFile import descendantClass
#from .myClassFile import myClass
#import pickle

def main():
    i=1
    classContainerExemplar = classContainer()
    menu={}
    menu['1']=classContainerExemplar.addClass
    menu['2']=classContainerExemplar.addDescendantClass
    menu['3']=classContainerExemplar.editClassParam
    menu['4']=classContainerExemplar.showList
    menu['5']=classContainerExemplar.writeListInFile
    menu['6']=classContainerExemplar.readListFromFile
    menu['7']=classContainerExemplar.clearList
    while i!='0':
        print("1-добавить экземпляр класса родителя в лист\n 2 -добавить экземпляр класса наследника в лист  \n 3-редактировать выбранный экземпляр \n 4-вывести список \n 5-записать в файл \n 6- считать с файла \n 7- очистить лист\n 0 - выход ")
        i=input()
        if i!='0':
            menu[i]()

if __name__=="__main__":
    main()


