def main():
    infile = open('input.txt', "r")
    outfile = open('output.txt', "w")
    age = 999
    youngest = ''
    print('Name of Youngest Person is: ', file=outfile, end='')

    for line in infile:
        line = line.rstrip()
        list1 = line.split(' ')
        next_name = list1[1]
        next_age = int(list1[2])
        if next_age < age:
            age = next_age
            youngest = next_name
    print('Name of Youngest Person is: {0}'.format(youngest))
    print(youngest, file=outfile)

main()