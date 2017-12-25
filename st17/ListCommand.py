def MenuFunction(l):
    l()

def ShowList():
    return WhileTest(IsInt,"""
0 - добавить обычное блюдо
1 - добавить VIP блюдо
2 - редактировать блюдо
3 - очистить меню
4 - вывести на экран меню
5 - сохранить меню в файл
6 - загрузить меню из файла
other numbers - выход
""")

def WhileTest(f,s):
    while(True):
        v=input(s)
        if f(v):
            return v

def IsInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def IsFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def IsFile(value):
    try:
        open("st17/"+value, 'rb')
        return True
    except FileNotFoundError:
        return False



