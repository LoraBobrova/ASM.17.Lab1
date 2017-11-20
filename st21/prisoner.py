class Prisoner:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._age = None

    def input_data(self):
        self._first_name = input("First name: ")
        self._last_name = input("Last name: ")
        self._age = input("Age: ")

    def output_data(self):
        print("First name: " + self._first_name)
        print("Last name: " + self._last_name)
        print("Age: " + self._age)

    def edit(self):
        self._first_name = input("New first name: ")
        self._last_name = input("New last name: ")
        self._age = input("New age: ")
