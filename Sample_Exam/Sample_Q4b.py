def countEvenDigits(number):
    if number < 10:
        if number % 2 == 0:
            return 1
        else:
            return 0
    else:
        last = number % 10
        rest = int(number/10)
        if last % 2 == 0:
            return 1 + countEvenDigits(rest)
        else:
            return 0 + countEvenDigits(rest)



def main():
    x = int(input("Enter number:"))
    count = countEvenDigits(x)
    print("Number of even digits in {0} is {1}".format(x, count))


main()

