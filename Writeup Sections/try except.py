while True:
    try:
        integerInput = int(input("Enter an integer: "))
        break

    except ValueError:
        print("That's not a number. ")