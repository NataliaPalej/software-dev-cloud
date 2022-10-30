def main():
    word = str(input('Enter Word: ')).lower()
    target = str(input('Enter Target Letter: '))
    result = count_letter(word, target[0])
    print('{0} occurs in list {1} Times'.format(target[0], result))


def count_letter(word, target):
    result = 0
    for i in word:
        if i.lower() == target:     # ignore lower/upper case
            result += 1
    return result


main()

