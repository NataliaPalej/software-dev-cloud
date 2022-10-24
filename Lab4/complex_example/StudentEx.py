class Student:
    def __init__(self, name, ID, international):
        self.__name = name
        self.__ID = ID
        self.__present = 0
        self.__absent = 0
        self.__excused = 0
        self.__international = international

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_present(self):
        return self.__present

    def get_absent(self):
        return self.__absent

    def get_excused(self):
        return self.__excused

    def get_international(self):
        return self.__international

    def get_percent_attendance(self):
        if (self.__present + self.__absent + self.__excused) == 0:
            return 0
        else:
            return int(100 * (self.__present / (self.__present + self.__absent + self.__excused)))

    def mark_present(self):
        self.__present += 1

    def mark_absent(self):
        self.__absent += 1

    def mark_excused(self, days_excused):
        self.__excused += days_excused
