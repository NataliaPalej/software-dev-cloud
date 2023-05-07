def main():
    infile = open('input.txt', "r")
    outfile = open('output.txt', "w")
    lowest_age = 999
    youngest = ''
    print('Name of Youngest Person is: ', file=outfile, end='')

    for line in infile:
        line = line.rstrip()
        list1 = line.split(' ')
        name = list1[1]
        age = int(list1[2])

        if age < lowest_age:
            lowest_age = age
            youngest = name
    print('Name of Youngest Person is: {0}'.format(youngest))
    print(youngest, file=outfile)


main()
