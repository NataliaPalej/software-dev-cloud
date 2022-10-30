def decrement(val):
    if val < 0:
        raise ValueError
    elif val == 0:
        raise Exception
    else:
        val -= 1
        return val


def main():
    val = int(input("Enter value: "))
    try:
        res = decrement(val)
        print(res)
        print("Value entered: {0}".format(val))
        res = decrement(val)
        print("Result = {0}".format(res))
        res2 = decrement(res)
        print("Result = {0}".format(res2))
        res3 = decrement(res2)
        print("Result = {0}".format(res3))
        res4 = decrement(res3)
        print("Result = {0}".format(res4))
    except ValueError:
        print("Value cannot be negative")
    except Exception:
        print("Value already 0")


main()