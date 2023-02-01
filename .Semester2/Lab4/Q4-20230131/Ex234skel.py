class Shape:
    def __init__(self, width):
        self._width = width

    def readType(self):
        return 'Base Shape'

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, width):
        super().__init__(width)

    def readType(self):
        return 'Square'

    def area(self):
        return self._width * self._width


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__(width)
        self.__length = length

    def readType(self):
        return 'Rectangle'

    def area(self):
        return self._width * self.__length


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base)
        self.__height = height

    def readType(self):
        return 'Triangle'

    def area(self):
        return (1 / 2 * self._width) * self.__height


def main():
    obj1 = Square(5)
    obj2 = Rectangle(5, 6)
    obj3 = Triangle(5, 6)
    list1 = [obj1, obj2, obj3]
    for i in list1:
        print('Type:', i.readType())
        print('Area =', i.area(), '\n')


main()
