class Height:
    def __init__(self, feet, inch):
        self.feet = feet
        self.inch = inch

    def printHeight(self):
        print("{0}FT - {1}\'\'".format(self.feet, self.inch))

    def __add__(self, other):
        feet = self.feet + other.feet
        inch = self.inch + other.inch
        if inch >= 12:
            feet += 1
            inch -= 12
        return Height(feet, inch)

    def __eq__(self, other):
        if self.feet == other.feet and self.inch == other.inch:
            return True
        else:
            return False


def main():
    h1 = Height(2, 6)
    h2 = Height(3, 11)
    h3 = Height(3, 11)

    res = h1+h2
    print("2FT-6\'\' + 3FT-11\'\' = ", end="")

    res.printHeight()

    if (h1 == h2):
        print("(2-6) == (3-11)")
    if (h2 == h3):
        print("(3-11) == (3-11)")

main()

