class Stepper:

    def __init__(self, val):
        self._value = val

    def stepDown(self, amount):
        if amount <= self._value:
            self._value -= amount
            return True
        else:
            return False

    def getValue(self):
        return self._value


# Extended Class
class MyStepper(Stepper):
    def __init__(self, val, lim):
        super().__init__(val)
        self.__lim = lim

    def stepUp(self, val):
        if self.__lim >= self._value + val:
            self._value += val
            return True
        else:
            return False

    def getLimit(self):
        return self.__lim

    def resetLimit(self, amt):
        self.__lim = amt

