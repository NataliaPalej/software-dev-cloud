class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def getName(self):
        return self.__name

    def getBalance(self):
        return self.__balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt


