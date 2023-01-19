def calculate(value1, value2):
    if value2 == 0:
        raise Exception
    else:
        result = value1/value2
        return result


def main():
    val1 = int(input("Enter first: "))
    val2 = int(input("Enter second: "))
    try:
        result = calculate(val1, val2)
        print("{0} divided by {1} = {2}".format(val1, val2, result))
    except:
        print("Divide by Zero Exception")


main()

