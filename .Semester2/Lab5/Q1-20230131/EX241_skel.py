def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4}
    # Merging two lists together
    set3 = set1.union(set2)
    target = int(input('Enter Target: '))
    result = mySearch(set3, target)
    print('Element {0} found in at least 1 set = {1}'.format(target, result))


def mySearch(setp3, tar):
    result = False
    for i in setp3:
        if i == tar:
            result = True
    return result


main()
