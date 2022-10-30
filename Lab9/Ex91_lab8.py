def power(b, p):
    if p == 0:
        return 1
    else:
        return b*power(b, p-1)


def main():
    b = int(input('Enter base: '))
    p = int(input('Enter power: '))
    result = power(b, p)
    print('\n{0}^{1} = {2}'.format(b, p, result))


main()
