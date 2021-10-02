# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 09:45:48 2021

@author: jakir
"""

###########
# Book
###########

###
# Example: Inheritance - MIT Person
###

import datetime

class Person(object):
    
    def __init__(self, name):
        """
        Create a person

        """
        self.name = name
        
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        
        self.birthday = None
        
        
    def getName(self):
        """
        Returns self's full name

        """
        return self.name
     
    def getLastName(self):
        """
        Returns self's last name

        """
        return self.lastName
    
    def setBirthday(self, birthdate):
        """
        Assumes birthdate of type datetime.date
        Set's self's birthday to birthdate

        """
        
        self.birthday = birthdate
    
    def getAge(self):
        """
        Returns self's current age ind days

        """
        if self.birthday == None:
            raise ValueError
        else:
            return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """
        Returns True if self preceds other in alphabetical order on last
        names, but if they are same full names are compared.

        """
        if self.lastName == other.lastName:
            return self.name < other.name
        
        return self.lastName < other.lastName
    
    def __str__(self):
        """
        Returns self's name

        """
        return self.name


# subclass of parent class
class MITPerson(Person):
    
    nextIdNum = 0 # identification number
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def isStudent(self, other):
        return isinstance(self, other)
    
# p1 = MITPerson("Barbara Beaver")
# print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
    
# p2 = MITPerson("Justin Beaver")
# print(str(p2) + '\'s id number is ' + str(p2.getIdNum()))

# p1 = MITPerson("Mark Guttag")
# p2 = MITPerson("Billy Bob Beaver")
p3 = MITPerson("Billy Bob Beaver")
# p4 = Person("Billy Bob Beaver")

# print("p1 < p2 =", p1 < p2)
# print("p3 < p2 =", p3 < p2)
# print("p4 < p1 =", p4 < p1)

# # print("p1 < p4 =", p1 < p4) # AttributeError: Person object has no attribute idName


class Student(MITPerson):
    pass

class UG(Student):
    
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.classYear = classYear
        
    def getClass(self):
        return self.classYear
    
class Grad(Student):
    pass
    # pass indicates this class has no attributes other
    # than those are inherited from superclass.

p5 = Grad("Buzz Aldrin")
p6 = UG("Billy Beaver", 1984)

# print(p5,"is a graduate student =", type(p5) == Grad)
# print(p5, "is a undergraduate student =", type(p5) == UG)

# print(p5, "is a student is", p5.isStudent(Student))
# print(p6, "is a student is", p6.isStudent(Student))
# print(p3, "is a student is", p3.isStudent(Student))

class TransferStudent(Student):
    
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool
    
    def getOldSchool(self):
        return self.fromSchool

p7 = TransferStudent("David Malan", "Harvard University")
# print(p7, "is a student is", p7.isStudent(Student))


class Grades(object):
    
    def __init__(self):
        """
        Creates empty grade book.

        """
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        """
        Assumes student of type Student. Add student to the grade book.

        """
        
        if student in self.students:
            raise ValueError("Duplicate student")
        
        self.students.append(student)
        self.grades[self.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """
        Assumes grade is a float. Add grade to the list of grades for student.

        """
        try:
            self.grades[student.getIdNum()] = grade
        except:
            raise ValueError("Student not in mapping.")
            
    def getGrades(self, student):
        """
        Returns a list of grades for student.

        """
    
        try:
            return self.grades[student.getIdNum()][:] # return copy of grades
        except:
            raise ValueError("Student not in mapping.")
    
    def getStudents(self):
        """
        Returns a sorted list of students in the grade book
        """
        
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # return copy of list of students
    
    





