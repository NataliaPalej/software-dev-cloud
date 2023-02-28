class MyList:
    def __init__(self,list):
        self._list = list

    def linearSearch(self, target):
        result = False
        # Go through the list
        for i in self._list:
            # If target found, return true
            if  i == target:
                result = True
        return result

    def readList(self):
        list = ""
        for i in self._list:
            list += str(i) + ', '
        return list





