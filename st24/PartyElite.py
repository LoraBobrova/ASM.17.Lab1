from .Comrade import Comrade


class PartyElite(Comrade):

    __position = None

    def __init__(self, list):
        super().__init__(list)

    def input(self):
        super().input()
        self.__position = input("Position: ")

    def edit(self):
        super().edit()
        self.__position = input("Position: ")

    def output(self):
        super().output()
        print("Position: " + self.__position)

