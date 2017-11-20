from .overseer import *
import pickle


class Prison:
    FILENAME = "st21/storage.pkl"
    
    def __init__(self):
        self._stack = []

    def _add_person(self, person):
        person.input_data()
        self._stack.append(person)

    def add_prisoner(self):
        self._add_person(Prisoner())
        print("Prisoner has been added")
    
    def add_overseer(self):
        self._add_person(Overseer())
        print("Overseer has been added")

    def print_list(self):
        if len(self._stack) != 0:
            for i, person in enumerate(self._stack):
                print("ID: ", i)
                person.output_data()
                print()
        else:
            print("List is empty")
   
    def clear_list(self):
        self._stack.clear()
        print("All list has been cleared")

    def edit_person(self):
        pers_id = input("Enter persons ID to edit: ")
        try:
            self._stack[int(pers_id)].edit()
        except ValueError:
            print("You should enter an integer value")
        except IndexError:
            print("There is no such index")
        else:
            print('Person with ID ' + pers_id + ' has been removed')

    def remove_person(self):
        pers_id = input("Enter person ID to delete: ")
        try:
            del self._stack[int(pers_id)]
        except ValueError:
            print("You should enter an integer value")
        except IndexError:
            print("There is no such index")
        else:
            print("Prisoner with ID " + pers_id + " has been removed ")

    def write_to_file(self):
        if len(self._stack) != 0:
            print("Writing to " + Prison.FILENAME)
            try:
                with open(Prison.FILENAME, "wb") as f:
                    pickle.dump(self._stack, f)
            except FileNotFoundError:
                print("Bad file directory")
            else:
                print("Writing has been completed")
        else:
            print ("List is empty")

    def read_from_file(self):
        print("Reading from " + Prison.FILENAME)
        try:
            with open(Prison.FILENAME, "rb") as f:
                self._stack = pickle.load(f)
        except FileNotFoundError:
            print("Can't find the file")
        else:
            print("Reading has been completed")
