def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4, 5, 6, 7}
    target1 = int(input('Enter Target 1: '))
    target2 = int(input('Enter Target 2: '))
    result = inBoth(set1, set2, target1, target2)
    print('Element {0} & {1} found in both sets = {2}'.format(target1, target2, result))


def inBoth(setp1, setp2, tar1, tar2):
    # Merging two lists together
    set3 = setp1.intersection(setp2)
    # Creating list of two targets
    set4 = {tar1, tar2}
    # Checking if targets are in the list
    result = set4.issubset(set3)
    return result


main()
