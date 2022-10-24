def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = count_even(list1)
    print("Number of even numbers in the list is {0}".format(result))


def count_even(list1):
    count = 0
    for i in list1:
        if i % 2 == 0:
            count = count + 1
            print(i)
    return count


main()
