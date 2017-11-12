from st24.CommunistParty import CommunistParty

communist_party = CommunistParty()

menu = {
    "1": ("Add comrade", communist_party.add_comrade),
    "2": ("Add part elite", communist_party.add_party_elite),
    "3": ("Edit comrade", communist_party.edit),
    "4": ("Print party list", communist_party.print_party_list),
    "5": ("Write list to file", communist_party.write_to_file),
    "6": ("Read list from file", communist_party.read_from_file),
    "7": ("Remove comrade", communist_party.remove),
    "8": ("Clear list", communist_party.clear_party_list),
    "9": ("Exit", None)
}


def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])

        try:
            user_input = input()
            if user_input == "9":
                break
            else:
                menu[user_input][1]()
        except Exception as ex:
            print("Exception is ", ex)


if __name__ == "__main__":
    main()
