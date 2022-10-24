def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input("Enter lower limit: " ))
    upper = int(input("Enter upper limit: " ))
    result = all_in_range(list1, lower, upper)
    print("{0} = all elements are between {1} and {2} inclusive".format(result, lower, upper))

def all_in_range(list, low, high):
    for i in list:
        if low < i and high > i:
            return True
        return False


main()
3
