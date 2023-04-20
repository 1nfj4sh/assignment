from grade import Grade
from load import Load

students = []
teachers = []

def addRecordStudent():
    while True:
        print()
        id = input('Enter ID: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        lastName = input('Enter last name: ')
        type = input('Enter type: ')
        year = input('Enter year: ')
        course = input('Enter course: ')
        section = input('Enter section: ')
        print()
        filipino = input('Enter grade in Filipino: ')
        math = input('Enter grade in Math: ')
        science = input('Enter grade in Science: ')
        english = input('Enter grade in English: ')

        std = Grade(filipino, math, science, english)
        std.id = id
        std.firstName = firstName
        std.middleName = middleName
        std.lastName = lastName
        std.type = type
        std.year = year
        std.course = course
        std.section = section

        students.append(std)

        print()
        answer = input('Do you want to try again? (y/n): ')

        if (answer != 'y'): 
            break 

    menu()

def addRecordTeacher():
    while True:
        print()
        id = input('Enter ID: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        lastName = input('Enter last name: ')
        type = input('Enter type: ')
        department = input('Enter department: ')
        position = input('Enter position: ')
        subject = input('Enter subject: ')

        tch = Load(subject)
        tch.id = id
        tch.firstName = firstName
        tch.middleName = middleName
        tch.lastName = lastName
        tch.type = type
        tch.department = department
        tch.position = position

        teachers.append(tch)

        print()
        answer = input('Do you want to try again? (y/n): ')

        if (answer != 'y' or 'Y'):
            break

    menu()

def deleteRecordStudent():
    i = int(input('Enter Index: '))
    students.pop(i)
    menu()

def deleteRecordTeacher():
    i = int(input('Enter Index: '))
    teachers.pop(i)
    menu()

def searchRecordStudent():
    i = int(input('Enter index: '))
    print()
    print(f'{i} \t {students[i].getName()} \t | \t {students[i].getYrCrsSec()} \t | \t {students[i].getAve()}')
    menu()

def searchRecordTeacher():
    i = int(input('Enter index: '))
    print(f'{i} \t {teachers[i].getName()} \t | \t {teachers[i].getDepartment()} \t | \t {teachers[i].getPosition()} \t | \t {teachers[i].getSubject()}')
    menu()

def displayRecordStudent():
    print()
    print('-----------------------------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t {s.getName()} \t | \t {s.getYrCrsSec()} \t | \t {s.getAve()}')
        i += 1
    print('-----------------------------------------------------------------------------------------------------')

def displayRecordTeacher():
    print()
    print('--------------------------------------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t {t.getName()} \t | \t {t.getDepartment()} \t | \t {t.getPosition()} \t | \t {t.getSubject()}')
        i += 1
    print('--------------------------------------------------------------------------------------------------------------')

def menu():
    print()
    print()
    print('Select one: ')
    print()
    print('     Student')
    print('     Teacher')
    print('     Skip')
    print()
    choice = input('Enter answer: ')
    if (choice == 'Student'):
        stud()
    elif (choice == 'Teacher'):
        teach()
    elif (choice == 'Skip'):
        skip()

def stud():
    while True:
        print()
        print('Menu')
        print('A = Add Student       S = Search Student')
        print('D = Delete Student    M = Display Student')
        print()

        choice = input('Enter a function: ')
        if (choice == 'A'):
            addRecordStudent()
        elif (choice == 'D'):
            deleteRecordStudent()
        elif (choice == 'S'):
            searchRecordStudent()
        elif (choice == 'M'):
            displayRecordStudent()
            menu()
            
        print()

def teach():
    while True:
        print()
        print('Menu')
        print('F = Add Teacher       C = Search Teacher')
        print('G = Delete Teacher    N = Display Teacher')
        print()

        choice = input('Enter a function: ')
        if (choice == 'F'):
            addRecordTeacher()
        elif (choice == 'G'):
            deleteRecordTeacher()
        elif (choice == 'C'):
            searchRecordTeacher()
        elif (choice == 'N'):
            displayRecordTeacher()
            menu()
        print()

def skip():
    while True:
        print()
        print('Menu')
        print('X = Display all      Z = Delete all')
        print()

        choice = input('Enter a function: ')
        print()
        if (choice == 'X'):
            print()
            print('Student List: ')
            displayRecordStudent()
            print()
            print('Teacher List: ')
            displayRecordTeacher()
            print()
            menu()
        elif (choice == 'Z'):
            students.clear()
            teachers.clear()
            menu()   
        print()
menu()