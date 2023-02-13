class Height:
    def __init__(self, f, i):
        self.feet = f
        self.inches = i

    def printHeight(self):
        print('{0}\'-{1}\"'.format(self.feet, self.inches))

    def __add__(self, other):
        result = Height(self.feet + other.feet, self.inches + other.inches)
        if result.inches >= 12:
            result.feet += 1
            result.inches -= 12
        return result

    def __isub__(self, other):
        result = Height(self.feet - other.feet, self.inches - other.inches)
        if result.inches < 0:
            result.feet -= 1
            result.inches += 12
        return result

    def __eq__(self, other):
        if self.inches == other.inches and self.feet == other.feet:
            return True
        else:
            return False


def main():
    h1 = Height(5, 10)
    h2 = Height(5, 10)
    h3 = Height(8, 5)
    res1 = h1 + h3
    print('5ft 10ins + 8ft 5ins = ', end='')
    res1.printHeight()

    h3 -= h2
    print('8ft 1ins -= 5ft 9ins= ', end='')
    h3.printHeight()

    if h1 == h2:
        print('Both 5ft 10ins')

    if h1 == h3:
        print('Both are not 5 ft 10 ins')


main()
