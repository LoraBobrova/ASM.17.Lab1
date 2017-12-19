from .Car import Car
from .Supercar import Supercar
import pickle


class Autocenter:

    FILENAME = "st36/dump.pkl"

    def __init__(self):
        self._autocenter = []

    def _add_auto(self, auto):
        auto.console_input()
        self._autocenter.append(auto)
        print("Done")

    def add_car(self):
        self._add_auto(Car())

    def add_supercar(self):
        self._add_auto(Supercar())

    def print_autocenter(self):
        for i, auto in enumerate(self._autocenter):
            print("ID: ", i)
            auto.console_output()
            print()

    def clear_autocenter(self):
        self._autocenter.clear()
        print("Autocenter list cleared")

    def edit_auto(self):
        id = input("Auto ID to edit: ")
        self._autocenter[int(id)].edit()

    def remove_auto(self):
        id = input("Auto ID to delete: ")
        del self._autocenter[int(id)]
        print("Auto with ID# " + id + " removed ")

    def write_to_file(self):
        print("Writing to " + Autocenter.FILENAME)
        with open(Autocenter.FILENAME, "wb") as f:
            pickle.dump(self._autocenter, f)
        print("Done")

    def read_from_file(self):
        print("Reading from " + Autocenter.FILENAME)
        with open(Autocenter.FILENAME, "rb") as f:
            self._autocenter = pickle.load(f)
        print("Done")
