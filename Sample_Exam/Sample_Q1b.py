def main():
    base = int(input("Enter Base: "))
    pow = int(input("Enter Power: "))
    result = power(base, pow)
    print("{0} to power of {1} = {2}".format(base, pow, result))


def power(b, p):
    result = 1
    for i in range (1, p+1):
        result = result*b
    return result

main()
