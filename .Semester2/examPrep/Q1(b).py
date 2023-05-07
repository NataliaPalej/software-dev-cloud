def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4, 5, 6, 7}
    target1 = int(input("Enter target1: "))
    target2 = int(input("Enter target2: "))
    result = inBoth(set1, set2, target1, target2)
    print("Element {0} & {1} found in both sets: {2}".format(target1, target2, result))


def inBoth(setp1, setp2, tar1, tar2):
    result = 0
    if tar1 in setp1 and tar1 in setp2 and tar2 in setp1 and tar2 in setp2:
        result += 1
        return True
    else:
        result += 0
        return False

main()

