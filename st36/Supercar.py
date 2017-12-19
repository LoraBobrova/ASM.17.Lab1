from .Car import Car


class Supercar(Car):
    def __init__(self):
        super().__init__()
        self._nitro = None
        self._modification = None

    def console_input(self):
        super().console_input()
        self._nitro = input("Nitro: ")
        self._modification = input("Modification: ")

    def console_output(self):
        super().console_output()
        print("Nitro: " + self._nitro)
        print("Modification: " + self._modification)

    def edit(self):
        super().edit()
        self._nitro = input("New nitro: ")
        self._modification = input("New modification ")
