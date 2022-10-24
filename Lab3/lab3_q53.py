def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    number = int(input("Enter number: "))
    result = count_target(list1, number)
    print("{0} repeated {1} times".format(number, result))


def count_target(list1, number):
    count = 0
    for i in list1:
        if i == number:
            count = count + 1
            print(i)
    return count


main()
