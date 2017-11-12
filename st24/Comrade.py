class Comrade:
    __name = None
    __party_name = None
    id = None

    def __init__(self, list):
        self.id = list.get_id()

    def input(self):
        self.__name = input("Fullname: ")
        self.__party_name = input("Party name: ")

    def edit(self):
        self.__name = input("Fullname: ")
        self.__party_name = input("Party name: ")

    def output(self):
        print("ID: " + str(self.id))
        print("Fullname: " + self.__name)
        print("Party name: " + self.__party_name)
