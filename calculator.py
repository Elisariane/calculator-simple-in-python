def printMenuOptions():
    print("ºººººThe Simple Calculatorººººº")
    print("Choose the operation...")
    print("1 - sum")
    print("2 - subtraction")
    print("3 - division")
    print("4 - multiplication")
    print("0 - Exit")


def add(enter_number_one, enter_number_two):
    return enter_number_one + enter_number_two


def subtraction(enter_number_one, enter_number_two):
    return enter_number_one - enter_number_two


def division(enter_number_one, enter_number_two):
    return enter_number_one / enter_number_two


def multiplication(enter_number_one, enter_number_two):
    return enter_number_one * enter_number_two


def printTotal(total):
    print("TOTAL = {:.2f} ".format(total))


def menu():
    printMenuOptions()
    choice = int(input("Enter your choose: "))
    while choice != 0:
        if choice == 0 or choice >= 5:
            print("Exit...")
            break
        chooseTheOperation(choice)
        printMenuOptions()
        choice = int(input("Enter your choose: "))


def chooseTheOperation(choice):
    enter_number_one = float(input("Enter number: "))
    enter_number_two = float(input("Enter number: "))
    if choice == 1:
        printTotal(add(enter_number_one, enter_number_two))
    elif choice == 2:
        printTotal(subtraction(enter_number_one, enter_number_two))
    elif choice == 3:
        printTotal(division(enter_number_one, enter_number_two))
    elif choice == 4:
        printTotal(multiplication(enter_number_one, enter_number_two))
    else:
        print("ERROR. Could not execute operation")


menu()
