def main():
    #open file with file name
    infile= open('input5.txt',"r")
    #output file
    outfile = open('output5.txt', "w")

    #read lines
    line = infile.readline()
    line = infile.readline()

    #print start of the output
    print('List of Overall Marks=: ', file=outfile)
    print('----------------------- ', file=outfile)

    #go through the lines
    for i in infile:
        # Split the file to print the name
        i.rstrip()
        list1 = i.split(' ')
        name = list1[0]
        print("Name: {0}".format(name))

        # Split the file to print the numbers
        list2 = list1[1].split(';')
        val1 = int(list2[0])
        #print(val1)
        val2 = int(list2[1])
        #print(val2)
        val3 = int(list2[2])
        #print(val3)
        val4 = int(list2[3])
        #print(val4)
        print("Results: {0}, {1}, {2}, {3}".format(val1, val2, val3, val4))

        average = int((val1+val2+val3+val4)/4)
        print('Average: {0}'.format(average))


main()
