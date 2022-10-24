def search(list, number):
    result = False
    for i in list:
        if i == number:
            result = True
        return result


def my_largest(list):
    return max(list)


def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = my_largest(list1)
    print("{0} is the largest".format(result))



main()