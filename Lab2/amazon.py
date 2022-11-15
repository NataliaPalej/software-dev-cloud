def numbers_to_reverse():
    list_to_reverse = [[24, 1], [4358, 754], [305, 794]]
    output = 0
    for i in list_to_reverse: #list_to_reverse = [[24,1], [4358, 754], [305, 794]]
        # i = [24,1]
        reversed_numbers = []
        for j in i: # j = 24, 1
            reversed_numbers += reversed(j)  # reversed_number = 42, 1 / j = 24,1
        # reversed_numbers = [42, 1]
        sum_reversed = reversed_numbers[0] + reversed_numbers[1] # 43
        output = reversed(sum_reversed) # => 34, sum_reversed = 43
        print(output)




# 4358
def reversed(number): # 4358
    string_number = str(number) # [4358] "4358"
    print(string_number)
    size = len(string_number) # 4
    print(size)
    rev_numbers = []
    # print(size)
    for i in range(size, 0, -1): # traverses the list backwards: i = 3, 2, 1, 0
        print(string_number[i])
        rev_numbers += string_number[i] # [8, 5, 3, 4]
    return int(rev_numbers)



numbers_to_reverse()
# list_to_reverse = [[24,1], [4358, 754], [305, 794]]
