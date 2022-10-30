from enum import IntEnum


class Shape(IntEnum):       # assign option number
    Add = 1
    Sub = 2
    Mult = 3


def main():
    x = int(input('Enter Value1:'))
    y = int(input('Enter Value2:'))
    print("\nOptions\n---------\nAdd: Enter {0}\nSub: Enter {1}"
          "\nMult: Enter {2}".format(Shape.Add, Shape.Sub, Shape.Mult))
    choice = int(input('Enter Choice: '))
    if choice == Shape.Add:
        print("\n{0} + {1} =".format(x, y), (x + y))
    elif choice == Shape.Sub:
        print("\n{0} - {1} =".format(x, y), (x - y))
    elif choice == Shape.Mult:
        print("\n{0} * {1} =".format(x, y), (x * y))


main()

