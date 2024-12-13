counter = 1

number = input("Enter a number between 1 and 100: ")

while 1 <= int(number) <= 100 and counter <= int(number):
    if counter % 3 == 0 and counter % 5 == 0:
        print("fizzbuzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")

    else:
        print(counter)
    counter = counter + 1

if int(number) < 1 or int(number) > 100:
    print("Invalid number!")