# function that outputs the largest entered number
def main():
    print("Enter two numbers and see which one is the largest:")
    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))
    if val1 > val2:
        ans = val1
        print("First value is the largest (", ans, ")")
    else:
        ans = val2
        print("Second value is the largest (", ans, ")")
    print(ans, "is the largest")
# calling the function
#main()


# function that takes three integers and prints the largest
def largest():
    print("Enter three numbers and see which one is the largest:")
    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))
    val3 = int(input("Enter third value: "))
    if val1 > val2 and val1>val3:
        ans = val1
    elif val2 > val1 and val2 > val3:
        ans = val2
    else:
        ans = val3
    print("Number ", ans, " is the largest")

#largest()


# function that gives user three options to add, multiply or substract
def calculate():
    print("Select option:\nEnter option 1 to add\nEnter option 2 to mupltiply\nEnter option 3 to substract")
    option = int(input())
    if option == 1:
        print("Enter two values to add")
        val1 = int(input("Enter first value: "))
        val2 = int(input("Enter second value: "))
        sum = val1+val2
        print(val1, " + ", val2, " = ", sum)
    elif option == 2:
        print("Enter two values to multiply")
        val1 = int(input("Enter first value: "))
        val2 = int(input("Enter second value: "))
        ans = val1*val2
        print(val1, " * ", val2, " = ", ans)
    elif option == 3:
        print("Enter two values to subtract")
        val1 = int(input("Enter first value: "))
        val2 = int(input("Enter second value: "))
        ans = val1 - val2
        print(val1, " - ", val2, " = ", ans)

#calculate()


# while loop that takes 5 numbers and adds them together
def loop():
    count = 0
    total = 0
    while (count < 5):
        value = int(input("Enter value: "))
        total += value
        count = count + 1
    print("Sum of entered values is: ", total)

#loop()


# while loop that casts numbers 65-75 into letters
def letter():
    print("| ---------------- |\n|   Ascii Table    |\n| ---------------- |\n| Letter |  Value  |")
    value = 65
    while value < 75:
        # cast value to character
        letter = chr(value)
        print("|  ", value, "  |   ", letter, "   |")
        value += 1
    print("| -E-N-D-| ------- |")

#letter()


# for loop that casts numbers 65-75 into letters
def letter1():
    print("| ---------------- |\n|   Ascii Table    |\n| ---------------- |\n| Letter |  Value  |")
    value = 65
    for value in range(65, 100):
        letter = chr(value)
        print("|  ", value, "  |   ", letter, "   |")
        value += 1
    print("| -E-N-D-| ------- |")
#letter1()


# enter name and print it 6 times
def name():
    entry = str(input("Enter name: "))
    for i in range(1, 7):
        print(i, ") Name: ", entry)


name()


