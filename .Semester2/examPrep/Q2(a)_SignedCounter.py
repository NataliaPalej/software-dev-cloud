class Counter:
    def __init__(self, val1):
        self._value = val1

    def setValue(self, val1):
        self._value = val1

    def getValue(self):
        return self._value


class Sign:
    def __init__(self, sign):
        self._sign = sign

    def setSign(self, sign):
        self._sign = sign

    def getValue1(self):
        return self._sign


class SignedCounter(Sign, Counter):
    def __init__(self, char, int):
        Sign.__init__(self, char)
        Counter.__init__(self, int)

    def print(self):
        print("Value: {0} {1}".format(self.getValue1(), self.getValue()))

    def reset(self, int, char):
        self.setSign(char)
        self.setValue(int)


def main():
    char_input = input("Enter a character: ")
    int_input = int(input("Enter an integer: "))
    sc = SignedCounter(char_input, int_input)
    sc.print()


main()