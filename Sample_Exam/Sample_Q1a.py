# Q1 (a)

def main():
    number = int(input("Enter value 1-99 (negative to stop): "))
    counter = 0

    while number >= 0:
        if number > 99:
            print("Please enter values between 1-99")
        if number < 10 and number > 0:
            counter += 1
        number = int(input("Enter value 1-99 (negative to stop): "))
    print("Sum of single digit elements: {0}".format(counter))


main()
