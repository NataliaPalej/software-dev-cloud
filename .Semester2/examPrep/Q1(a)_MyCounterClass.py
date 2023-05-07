class Counter:
    def __init__(self, val):
        self.value = val

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value

    def decrement(self):
        if self.value > 0:
            self.value -= 1
            return True
        else:
            return False


class MyCounter(Counter):
    def __init__(self, val, limit):
        super().__init__(val)
        self.limit = limit

    def getLimit(self):
        return self.limit

    def increment(self):
        if self.value < self.limit:
            self.value += 1
            return True
        else:
            return False


def main():
    limit = int(input("Enter the limit for the counter: "))
    counter = MyCounter(0, limit)

    choice = None
    while choice != "q":
        print(f"Counter value: {counter.getValue()}")
        print("Options: (i)ncrement, (d)ecrement, (q)uit")
        choice = input("Enter your choice: ")

        if choice == "i":
            if counter.increment():
                print("Counter incremented")
            else:
                print("Counter already at maximum value")

        elif choice == "d":
            if counter.decrement():
                print("Counter decremented")
            else:
                print("Counter already at minimum value")

        elif choice != "q":
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
