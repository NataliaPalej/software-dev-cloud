def main():
    set1 = {2, 5, 2, 8, 7}
    set2 = {1, 2, 3, 4, 5, 7}
    # Merges two lists together without duplicates
    set3 = set1.intersection(set2)
    result = countBoth(set3)
    print('# Unique Elements found in both sets = {0}'.format(result))


def countBoth(setp1):
    result = 0
    for i in setp1:
        result += 1
        print('{', i, '}')
    return result


main()
