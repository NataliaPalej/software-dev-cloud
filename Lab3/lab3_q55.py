def main():
    list1 = [2, 6, 2, 7, 8, 4, 2, 6]
    result = all_even(list1)
    print("Are all the numbers even in list1? {0}".format(result))

    list2 = [2, 6, 2, 8, 8, 4, 2, 6]
    result = all_even(list2)
    print("Are all the numbers even in list2? {0}".format(result))


def all_even(x):
    for i in x:
        if i % 2 != 0:
            return False
    return True


main()
