class Worker:
    def __init__ (self):
        self.type = 'Сотрудник'
        self.name = ''
        self.year = ''
        self.position = ''
        self.salary = ''

    def Write(self):
        self.name = input("Имя: ")
        self.year = input("Год рождения: ")
        self.position = input("Должность: ")
        self.salary = input("Оклад: ")


    def __str__(self):
        return '{}\nИмя: {}\nГод рождения: {}\nДолжность: {}\nОклад: {}\n'.format(self.type, self.name, self.year, self.position, self.salary)
