def calculate(val1, val2):
    if val2 == 0:
        return 0, True
    else:
        result = val1 / val2
        return result, False


def main():
    val1 = int(input("Enter val1: "))
    val2 = int(input("Enter val2: "))
    result, error = calculate(val1, val2)
    if not error:
        print("{0} / {1} = {2}".format(val1, val2, result))
    else:
        print("{0} / {1} = {2} --> Cannot divide by zero".format(val1, val2, result))


main()
