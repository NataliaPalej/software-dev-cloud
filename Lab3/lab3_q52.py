def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = add_odd(list1)
    print("Sum of odd numbers is {0}".format(result))


def add_odd(list1):
    sum = 0
    for i in list1:
        if i % 2 != 0:
            sum = sum + i
            print(i)
    return sum


main()
