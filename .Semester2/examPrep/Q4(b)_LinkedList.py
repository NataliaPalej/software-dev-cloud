class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

    def printNode(self):
        return '[' + self.name + ':' + str(self.age) + ']-->'


class MyList:
    def __init__(self):
        self.head = None

    def append(self, name, age):
        newNode = Node(name, age)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def sumOfAllAges(self):
        result = 0
        temp = self.head
        while temp is not None:
            result += temp.age
            temp = temp.next
        return result


def main():
    dict1 = {1: ["B", 33],
             2: ["C", 35],
             3: ["B", 21],
             4: ["E", 35],
             5: ["B", 44],
             6: ["C", 27]
             }

    # create a new linked list and append nodes
    mylist = MyList()
    for key, value in dict1.items():
        mylist.append(value[0], value[1])

    # print the sum of all ages in the linked list
    print("Sum of all ages:", mylist.sumOfAllAges())


if __name__ == '__main__':
    main()
