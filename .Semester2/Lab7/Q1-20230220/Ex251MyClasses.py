class Lecturer:
    def __init__(self, name, office):
        self._lecturer_name = name
        self._office = office
        
    def getName(self):
        return self._lecturer_name

    def getOffice(self):
        return self._office

    def updateOffice(self, office):
        self._office = office


class Module:
    def __init__(self, title, topic, lecturer_name, office):
        self._title = title
        self._topic = topic
        self._lecturer = Lecturer(lecturer_name, office)

    def readTitle(self):
        return self._title

    def updateTitle(self, title):
        self._title = title

    def readTopic(self):
        return self._topic

    # use getter method from class Lecturer to read name
    def readLecturerName(self):
        return self._lecturer.getName()

    # use getter method from class Lecturer to read office
    def readLecturerOffice(self):
        return self._lecturer.getOffice()

    # use method from class Lecturer to update office
    def updateLecturerOffice(self, office):
        self._lecturer.updateOffice(office)


        

