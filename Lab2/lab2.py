def main():
    #message()
    #print()
    #display("Hello,")
    #display("World!")
    #print()

    #Q30 Checks which value is the largest
    val1 = my_entry()
    val2 = my_entry()
    if (val1 > val2):
        print_message(val1)
    else:
        print_message(val2)

    #Q31 Outputs max value
    max_value = max(val1, val2)
    print("Max value is {0}".format(max_value))

    #Q32 Calculate sum of num you entered
    val1 = int(input('Enter Value to calculate its sum: '))
    result = sigma(val1)
    print('Sigma {0} = {1}'.format(val1, result))

    #Q33 Factorial Method
    val1 = int(input('Enter Value for factorial: '))
    result = factorial(val1)
    print("Factorial {0}! = {1}".format(val1, result))

    #Q34 Power Method
    entry1 = int(input("Enter base: "))
    entry2 = int(input("Enter power: "))
    result = power(entry1, entry2)
    print("{0} to power of {1} = {2}".format(entry1, entry2, result))

    #Q35
    entry1 = int(input("Enter base: "))
    entry2 = int(input("Enter power: "))
    result = power2(entry1, entry2)
    print("{0} to power of {1} = {2}".format(entry1, entry2, result))

    #Q36
    val1 = int(input("Enter value 1: "))
    val2 = int(input("Enter value 2: "))
    val3 = int(input("Enter value 3: "))
    result = largest(val1, val2, val3)
    print("{0} is the largest of 3 values you entered ({1}, {2}, {3})".format(result, val1, val2, val3))

    #Q37
    val1 = int(input("Enter height: "))
    result = vertical(val1)
    print("{0}".format(result))

    #Q38
    val1 = int(input("Enter width: "))
    horizontal(val1)

def message():
    print("Hello World!")

def display(var):
    print(var)

def my_entry():
    entry = int(input("Enter value: "))
    return entry

#Q30
def print_message(value):
    print("{0} is the largest".format(value))

#Q31
def max_number(value):
    print("{0} is the max value".format(value))

#Q32
def sigma(x):
    result = 0
    for value in range(1, x+1):
        result = result + value
    return result

#Q33
def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

#Q34
def power(a, b):
    result = 1
    for i in range(1, b+1):
        result = result * a
    #or it can be written:
    #result = pow(a, b)
    return result

#Q36
def largest(v1, v2, v3):
    result = 0
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v2
    else:
        return v3

#Q35
def power2(a, b):
    count = 0
    result = 1
    while (count < b):
        result = result * a
        count = count + 1
    return result

#Q37 print * in vertical line
def vertical(x):
    for i in range(1, x):
        result = "*"
        print(result)
    return result

#Q38 print * in horizontal line
def horizontal(x):
    count = 0
    while (count < x):
        result = ""
        count = count + 1
        print('*', end=" ")

main()



