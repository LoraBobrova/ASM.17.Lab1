from .Comrade import Comrade
from .PartyElite import PartyElite
import pickle


class CommunistParty:

    __path = "uploading_data.pkl"
    __party_list = []
    __id = 0

    def get_id(self):
        self.__id += 1
        return self.__id

    def add_comrade(self):
        comrade = Comrade(self)
        comrade.input()
        self.__party_list.append(comrade)
        print("Success")

    def add_party_elite(self):
        party_elite = PartyElite(self)
        party_elite.input()
        self.__party_list.append(party_elite)
        print("Success")

    def print_party_list(self):
        print()
        for compade in self.__party_list:
            compade.output()
            print()

    def write_to_file(self):
        with open(self.__path, "wb") as f:
            pickle.dump(self.__party_list, f)
        print("Excellent")

    def read_from_file(self):
        with open(self.__path, "rb") as f:
            self.__party_list = pickle.load(f)
        print("Excellent")

    def clear_party_list(self):
        self.__party_list.clear()
        print("Success")

    def remove(self):
        id = input("Id => ")
        try:
            del self.__party_list[next(i for i, x in enumerate(self.__party_list) if int(id) == x.id)]
        except StopIteration:
            print("Please, enter the correct ID")
        else:
            print("Success")

    def edit(self):
        id = input("Id => ")
        try:
            next(x for x in self.__party_list if int(id) == x.id).edit()
        except StopIteration :
            print("Please, enter the correct ID")
        else:
            print("Success")





