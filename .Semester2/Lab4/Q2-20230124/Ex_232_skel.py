class Operation:
    def __init__(self, val1):
        self._value1 = val1

    def op(self):
        return 0

    def readType(self):
        return 'Base Operation'

    def printData(self):
        print(self.readType())
        print('Initial Value= ', self._value1)


class Increment(Operation):
    def __init__(self, val1):
        super().__init__(val1)

    def op(self):
        return self._value1 + 1

    def readType(self):
        return 'Increment Operation'

    def printData(self):
        print(self.readType())
        print('Initial Value = ', self._value1)


class Decrement(Operation):
    def __init__(self, val1):
        super().__init__(val1)

    def op(self):
        return self._value1 - 1

    def readType(self):
        return 'Decrement Operation'

    def printData(self):
        print(self.readType())
        print('Initial Value = ', self._value1)


class Double(Operation):
    def __init__(self, val1):
        super().__init__(val1)

    def op(self):
        return self._value1 * 2

    def readType(self):
        return 'Double Operation'

    def printData(self):
        print(self.readType())
        print('Initial Value = ', self._value1)


def main():
    obj1 = Increment(1)
    obj2 = Decrement(4)
    obj3 = Double(6)
    list1 = [obj1, obj2, obj3]
    for i in list1:
        print('---------')
        i.printData()
        print('Result = ', i.op())


main()
