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
        return 'Square     '

    def area(self):
        return self._width * self._width


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        self._height = height

    def readType(self):
        return 'Rectangle'

    def area(self):
        return self._width * self._height


def main():
    shape = Shape(5)
    square = Square(5)
    rectangle = Rectangle(5, 2)

    list1 = [shape, square, rectangle]

    for i in list1:
        print("Shape: {0}\t\t\tArea: {1}".format(i.readType(), i.area()))

    #print("Type:\t\t\tArea: \n{0}\t\t\t{1}\n{2}\t\t\t\t{3}\n{4}\t\t\t{5}".format(shape.readType(), shape.area(),
    #                                                                             square.readType(), square.area(),
    #                                                                             rectangle.readType(),
    #                                                                             rectangle.area()))


main()
