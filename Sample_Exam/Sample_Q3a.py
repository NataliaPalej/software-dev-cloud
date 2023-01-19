class Treble:
    def __init__(self, value1, value2, value3):
        self.__value1 = value1
        self.__value2 = value2
        self.__value3 = value3

    def resetValue2(self, value2):
        self.__value2 = value2

    def getValue1(self):
        return self.__value1

    def getValue2(self):
        return self.__value2

    def getValue3(self):
        return self.__value3

    def add(self):
        return self.__value1 + self.__value2 + self.__value3

    def largest(self):
        return max(self.__value1, self.__value2, self.__value3)

