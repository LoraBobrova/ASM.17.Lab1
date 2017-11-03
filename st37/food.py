

class food:
    def __init__(self):
        pass
      
       

    def vvod(self):
        self.name = input('Введите название\n')
        self.quantity = input('Введите количество порций\n')
        self.calories = input('Введите каллорийность 1 порции\n')

    def vyvod(self):
        print('Блюдо - '+ self.name)
        print('Порций - '+ self.quantity)
        print('Каллорий в одной порции - '+ self.calories+ "\n" )
