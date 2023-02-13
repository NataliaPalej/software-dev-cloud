def main():
    # studentList= {'Smith':58, 'Jones':36, 'peters':78, 'Adams':44}
    student_list = {1234: 'Smith', 23123: 'Jones', 8834: 'Peters', 1212: 'Smith'}
    student_list.update({8292: 'Smith'})
    student_list.update({4321: 'Jones'})
    name = input('Enter Name to Search for: ')
    result = countOccurs(student_list, name)
    print('Student {0} occurs {1} times'.format(name, result))


def countOccurs(studentL, name):
    result = 0

    for key, value in studentL.items():
        if value == name:
            result += 1
        else:
            result += 0
    return result


main()
