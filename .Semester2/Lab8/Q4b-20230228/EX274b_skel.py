def main():
    infile1 = open('input4b1.txt', "r")
    infile2 = open('input4b2.txt', "r")
    outfile = open('output4b.txt', "w")
    total = 0

    print("Total of all values: ", file=outfile, end='')

    for line1 in infile1:
        line1.rstrip()
        list1 = line1.split(' ')
        val1 = int(list1[0])
        total += val1
        val2 = int(list1[1])
        total += val2

    for line2 in infile2:
        line2.rstrip()
        list2 = line2.split(' ')
        val3 = int(list2[0])
        total += val3
        val4 = int(list2[1])
        total += val4

    print(total, file=outfile)


main()
