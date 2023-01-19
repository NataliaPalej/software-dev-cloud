def main():
    word = "ballinasloe"
    target = str(input("Enter target letter: "))
    result1 = searchLetter(word, target)
    result2 = countLetter(word, target)
    print("\"{0}\" occurs in word: {1}".format(target, result1))
    print("\"{0}\" occurs in a word {1} times".format(target, result2))


def searchLetter(wordp, tar):
    result = False
    for i in wordp:
        if i == tar:
            result = True
    return result


def countLetter(wordp, tar):
    count = 0
    for i in wordp:
        if i == tar:
            count += 1
    return count

main()
