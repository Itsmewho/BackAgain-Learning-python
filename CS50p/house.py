name = input("What's your name? \n").lower().capitalize()

match name:
    case "Harry" | "Hermelien" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:  # The underscore is a catch all and or break statement in python
        print("That name is not known.")
