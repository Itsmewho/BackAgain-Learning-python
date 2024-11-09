# assignment is this number even or odd.


def main():

    number = int(input("What is the number: \n"))
    if even(number):
        print(f"You have given the {number} This number is a even number.")
    else:
        print(f"You have given the {number} This number is a odd number.")


def even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
