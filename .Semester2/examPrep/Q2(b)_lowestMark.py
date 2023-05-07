def main():
    studentList = {"Smith": 58, "Jones": 25, "Peters": 78, "Adams": 44}
    result = lowestMark(studentList)
    print("Student with lowest mark: {0}".format(result))


def lowestMark(studentL):
    lowest = 101
    name = ""
    for key, value in studentL.items():
        if value < lowest:
            lowest = value
            name = key
    return name


main()
