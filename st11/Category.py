class Category:
    def __init__(self):
        self.inp_tittle()

    def inp_tittle(self):
        self.tittle = input("Название категории: ")

    def output(self):
         print("Категория:", self.tittle)
        
    def print_cat(self):
            print('-Список категорий-')
            print(" ".join(["%s" % e for e in self.cat]))
