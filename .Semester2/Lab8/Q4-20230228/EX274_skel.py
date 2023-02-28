def main():
    infile = open('input4.txt', "r")
    outfile = open('output4.txt', "w")
    line = infile.readline()
    line = infile.readline()
    lowest = 999
    name_lowest = ''
    print('Name of Person with Lowest Overall Mark (CA + Exam) =: ', file=outfile, end='')

    for line in infile:
        list1 = line.split(' ')
        next_name = list1[0]
        next_ca = int(list1[1])
        next_exam = int(list1[2])
        overall = next_ca + next_exam
        if overall < lowest:
            lowest = overall
            name_lowest = next_name
    print(name_lowest, file=outfile)


main()
