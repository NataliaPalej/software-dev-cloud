class IndexTooHigh(Exception):
    pass


class IndexTooLow(Exception):
    pass


def read_value(list1, index):
    list_length = len(list1)
    print("List length: {0}".format(list_length))

    if index < 0:                   # error handling for index less than 0
        raise IndexTooLow
    elif index > list_length+1:     # error handling for index out of list
        raise IndexTooHigh
    else:
        val = list1[index]          # if no errors print value of asked index
        return val


def main():
    index = int(input("Enter index: "))
    list1 = [1, 3, 4, 5, 4, 6, 2]
    try:
        res = read_value(list1, index)
        print("Result = {0}".format(res))
    except IndexTooLow:
        print("Index Too Low")
    except IndexTooHigh:
        print("Index Too High")


main()
