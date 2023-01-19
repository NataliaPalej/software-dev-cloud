class Single:

    def __init__(self, val1):
        self._value1 = val1

    def incrValue1(self):
        self._value1 += 1

    def getValue1(self):
        return self._value1


# Extended Class Goes Here

class Pair(Single):
    def __init__(self, val1, val2):
        super().__init__(val1)
        self.__val2 = val2

    def incrValue2(self):
        self.__val2 += 1

    def getValue2(self):
        return self.__val2

    def add(self):
        return self._value1 + self.__val2

    def multiply(self):
        return self._value1 * self.__val2
