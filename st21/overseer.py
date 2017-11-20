from .prisoner import *


class Overseer(Prisoner):
    def __init__(self):
        super().__init__()
        self._salary = None
        self._phone_numb = None

    def input_data(self):
        super().input_data()
        self._salary = input("Salary: ")
        self._phone_numb = input("Phone number: ")

    def output_data(self):
        super().output_data()
        print("Salary: " + self._salary)
        print("Phone number: " + self._phone_numb)

    def edit(self):
        super().edit()
        self._salary = input("New salary: ")
        self._phone_numb = input("New phone number: ")
