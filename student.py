from person import Person

class Student(Person):
    def __init__(self, id, firstName, middleName, lastName, type, year, course, section):
        self.year = year
        self.course = course
        self.section = section
        
        Person.__init__(self, id, firstName, middleName, lastName, type)
   
    def getYrCrsSec(self):
        return f'{self.year}/{self.course}/{self.section}'
