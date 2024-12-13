print("Welcome to Unit Converter. With this version of the program you can currently convert kilometers into miles.")

while True:
    kilometers = input("Enter number of kilometers: ")
    miles = float(kilometers) * 0.621371

    print("This equals " + str(miles) + " miles.")

    question = input("Would you like to do another conversion? ")

    if question == "no":
        print("Goodbye!")
        break