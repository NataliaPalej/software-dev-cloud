class Complex:
    def __init__(self, r, i):
        self.real = r
        self.img = i

    def printComplex(self):
        print('({0}, {1})').format(self.real, self.img)

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)


def main():
    c1 = Complex(1, 2)
    c2 = Complex(3, 5)
    c_res = c1 + c2             # other words c1.__add__(c2)
    c_res.printComplex()
    print(c1)
    print(c2)
    print(c_res)
