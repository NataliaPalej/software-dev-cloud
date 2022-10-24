def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    result = add_range(list1, lower, upper)
    print("{0} = sum of elements between {1} and {2}".format(result, lower, upper))


def add_range(list1, low, high):
    sum = 0
    for i in list1:
        if i <= high and i >= low:
            sum = sum + i
            print(i)
    return sum


main()
