from person import Person

class Teacher(Person):
    def __init__(self, id, firstName, middleName, lastName, type, department, position):
        self.department = department
        self.position = position

        Person.__init__(self, id, firstName, middleName, lastName, type)

    def getDepartment(self):
        return self.department
    
    def getPosition(self):
        return self.position