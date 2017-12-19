from .Autocenter import Autocenter

autocenter = Autocenter()

EXIT_CODE = "9"

menu = {
    "1": ("Add car", autocenter.add_car),
    "2": ("Add supercar", autocenter.add_supercar),
    "3": ("Remove auto", autocenter.remove_auto),
    "4": ("Edit auto", autocenter.edit_auto),
    "5": ("Print list", autocenter.print_autocenter),
    "6": ("Write list to file", autocenter.write_to_file),
    "7": ("Read list from file", autocenter.read_from_file),
    "8": ("Clear list", autocenter.clear_autocenter),
    EXIT_CODE: ("Exit", None)
}


def main():
    while True:
        for key in menu:
            print(key + " " + menu[key][0])
        try:
            user_input = input(">>")
            if user_input == EXIT_CODE:
                break
            else:
                menu[user_input][1]()

        except Exception as ex:
            print("Exception raised: ", ex)


if __name__ == "__main__":
    main()
