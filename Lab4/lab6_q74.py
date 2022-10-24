from enum import IntEnum


class Shape(IntEnum):
    Add = 1
    Sub = 2
    Mult = 3


def main():
    x = int(input('Enter Value1:'))
    y = int(input('Enter Value2:'))
    print('\nOptions\n''---------\n''Add: Enter {0}'.format(Shape.Add),
          '\nSub: Enter {0}'.format(Shape.Sub), "\nMult: Enter {0}".format(Shape.Mult))
    choice = int(input('Enter Choice:'))
    if choice == Shape.Add:
        print("\n{0} + {1} =".format(x, y), (x + y))
    elif choice == Shape.Sub:
        print("\n{0} - {1} =".format(x, y), (x - y))
    elif choice == Shape.Mult:
        print("\n{0} * {1} =".format(x, y), (x * y))


main()

