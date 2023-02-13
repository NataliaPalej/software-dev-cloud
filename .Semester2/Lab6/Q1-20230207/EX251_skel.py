class Money:
    def __init__(self, e, c):
        self.euro = e
        self.cent = c

    def printMoney(self):
        print('€{0}.{1}'.format(self.euro, self.cent))

    def __add__(self, other):
        # add two values together
        result = Money(self.euro + other.euro, self.cent + other.cent)
        # if cents are over 100, reduce them and add to euro
        if result.cent >= 100:
            result.euro += 1
            result.cent -= 100
        return result

    def __gt__(self, other):
        # change euros to cents
        total1 = self.euro*100 + self.cent
        total2 = other.euro*100 + other.cent
        if total1 > total2:
            return True
        else:
            return False


def main():
    m1 = Money(2, 43)
    m2 = Money(3, 29)
    m3 = Money(4, 73)
    res1 = m1 + m2
    print('€2.43 + €3.29 = ', end='')
    res1.printMoney()

    res2 = m1 + m3
    print('\n€2.43 + €4.73 = ', end='')
    res2.printMoney()

    if m1 > m2:
        print('\n€2.43 > €3.29')
    if m3 > m1:
        print('\n€4.73 > €3.29')


main()
