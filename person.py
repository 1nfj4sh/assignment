class Person:
    def __init__(self,id,firstName,middleName,lastName,type):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.type = type
        
    def getName(self):
        return f'{self.id}, {self.firstName}, {self.middleName}, {self.lastName}, {self.type}'
        

