class Product:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getPrice(self):
        return self.__price

    def readType(self):
        return "Basic Product"

    def readDescription(self):
        return ""


class Car(Product):
    def __init__(self, make, model, price, engine):
        super().__init__(make, model, price)
        self.__engine = engine

    def readDescription(self):
        return "CC: " + str(self.__engine)

    def readType(self):
        return "Car"


class Laptop(Product):
    def __init__(self, make, model, price, description):
        super().__init__(make, model, price)
        self.__description = description

    def readDescription(self):
        return 'Screen: ' + str(self.__description) + "\'\'"

    def readType(self):
        return "Laptop"


class TV(Product):
    def __init__(self, make, model, price, description):
        super().__init__(make, model, price)
        self.__description = description

    def readDescription(self):
        return 'Screen: ' + str(self.__description) + "\'\'"

    def readType(self):
        return "TV"
