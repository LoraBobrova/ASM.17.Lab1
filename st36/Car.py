class Car:
    def __init__(self):
        self._model = None
        self._type= None
        self._color = None

    def console_input(self):
        self._model = input("Model: ")
        self._type = input("Type: ")
        self._color = input("Color: ")

    def console_output(self):
        print("Model: " + self._model)
        print("Type: " + self._type)
        print("Color: " + self._color)

    def edit(self):
        self._model = input("New Model: ")
        self._type = input("New Type: ")
        self._color = input("New Color: ")
