def main():
    infile = open('input3.txt', "r")
    outfile = open('output3.txt', "w")
    highest = 0
    print('Highest Overall Mark (CA + Exam) =: ', file=outfile, end='')

    for line in infile:
        l1 = line.split(' ')
        next_name = list[0]
        next_ca = int(l1[1])
        next_exam = int(l1[2])
        overall = next_ca + next_exam
        if overall > highest:
            highest = overall

    print(highest, file=outfile)


main()
