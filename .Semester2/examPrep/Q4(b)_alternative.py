class MyList:
    def __init__(self, list1):
        self._list = list1

    def binarySearch(self, target):
        LI = 0
        UI = len(self._list) - 1
        mid = int((LI + UI) / 2)
        found = False
        while found == False and LI <= UI:
            if target == self._list[mid]:
                found = True
            else:
                if target < self._list[mid]:
                    UI = mid - 1
                else:
                    LI = mid + 1
                mid = int((LI + UI) / 2)
        return found
