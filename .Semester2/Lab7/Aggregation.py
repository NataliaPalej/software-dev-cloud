class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print("({0}, {1})".format(self.x, self.y))


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__start = Point(x1, y1)
        self.__end = Point(x2, y2)

    def printLine(self):
        print("Line details:")
        print("- S T A R T -")
        self.__start.printPoint()
        print("--- E N D ---")
        self.__end.printPoint()


def main():
    l1 = Line(1, 4, 45, 1)
    l1.printLine()


main()

