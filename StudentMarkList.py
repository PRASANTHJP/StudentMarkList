# Defining  a class student, which contain
# name and Roll number and marks of the student

class Student(object):
    def __init__(self, name, roll, mark1, mark2):
        self.name = name
        self.roll = roll
        self.mark1 = mark1
        self.mark2 = mark2

    def getmarks(self):
        return self.mark1, self.mark2

    def getroll(self):
        return self.roll

    def __str__(self):
        return self.name + ' : ' + str(self.getroll()) + '  ::' + str(self.getmarks())


# Defining a function for building a Record
# which generates list of all the students
def Markss(rec, name, roll, mark1, mark2):
    rec.append(Student(name, roll, mark1, mark2))
    return rec


# Main Code
Record = []
x = 'y'
while x == 'y':
    name = input('Enter the name of the student: ')
    height = input('Enter the roll number: ')
    roll = input('Mark1: ')
    roll2 = input('Mark2: ')
    Record = Markss(Record, name, roll, roll2, height)
    x = input('another student? y/n: ')

# Printing the list of student
n = 1
for el in Record:
    print(n, '. ', el)
    n = n + 1
