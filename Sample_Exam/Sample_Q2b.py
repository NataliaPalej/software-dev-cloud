def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    lower = int(input("Enter lower limit: "))
    upper = int(input("Enter upper limit: "))
    result = addRange(list1, lower, upper)
    print("Result = {0}".format(result))


def countTarget(listp, tar):
    count = 0
    for i in listp:
        if i == tar:
            count += 1
    return count


def addRange(listp, lower, upper):
    result = 0
    for i in listp:
        if i >= lower and i <= upper:
            result = result + i
        else:
            result += 0
    return result

main()