class Base:
    def my_print(self):
        print("Base1")


class Derv1:
    def my_print(self):
        print("Derv1")


def main():
    obj = Base()
    obj1 = Derv1()

    list1 = [obj, obj1]

    for i in list1:
        i.my_print()


main()
