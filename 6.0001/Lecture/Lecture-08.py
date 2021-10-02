# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:14:37 2021

@author: jakir
"""

###
# Book
###

###
# Example: Set
###

# class IntSet(object):
#     """
#     An IntSet is a set of integers.
#     """
    
#     # Information about the implementation (not the abstraction)
#     # Value of the set is represented by a list of ints, self.values.
#     # Each int in the set occurs in self.values exactly once
    
    
#     def __init__(self):
#         """
#         Create an empty set of integers.

#         """
#         self.values = []
    
#     def insert(self, e):
#         """
#         Assumes e is an integer and insert e into the set

#         """
#         if e not in self.values:
#             self.values.append(e)

#     def member(self, e):
#         """
#         Assumes e is an integer. Return True if e is in self.values and False 
#         otherwise.

#         """
#         return e in self.values
        
#     def remove(self, e):
#         """
#         Assumes e is an integer and removes e from self. Raises ValueError
#         if e is not in self.

#         """
        
#         try:
#             self.values.remove(e)
#         except:
#             raise ValueError(str(e) + " not found")
            
            
#     def getMembers(self):
#         """
#         Returns a list containing the element of self. Nothing can be
#         assumed about the order of the elements.

#         """
#         return self.values[:]
            
#     def __str__(self):
        
#         self.values.sort()
#         result = ""
        
#         for e in self.values:
#             result = result + str(e) + ","
        
#         return "{" + result[:-1] + "}" # -1 omits trailing comma
            
            
            
# s = IntSet()
# s.insert(3)
# print(s.member(3))

# s.insert(4)
# print(s)


###
# Example: Keeping track of student and faculty
###

# import datetime

# class Person(object):
    
#     def __init__(self, name):
#         """
#         Create a person

#         """
#         self.name = name
        
#         try:
#             lastBlank = name.rindex(' ')
#             self.lastName = name[lastBlank+1:]
#         except:
#             self.lastName = name
        
#         self.birthday = None
        
        
#     def getName(self):
#         """
#         Returns self's full name

#         """
#         return self.name
     
#     def getLastName(self):
#         """
#         Returns self's last name

#         """
#         return self.lastName
    
#     def setBirthday(self, birthdate):
#         """
#         Assumes birthdate of type datetime.date
#         Set's self's birthday to birthdate

#         """
        
#         self.birthday = birthdate
    
#     def getAge(self):
#         """
#         Returns self's current age ind days

#         """
#         if self.birthday == None:
#             raise ValueError
#         else:
#             return (datetime.date.today() - self.birthday).days
    
#     def __lt__(self, other):
#         """
#         Returns True if self preceds other in alphabetical order on last
#         names, but if they are same full names are compared.

#         """
#         if self.lastName == other.lastName:
#             return self.name < other.name
        
#         return self.lastName < other.lastName
    
#     def __str__(self):
#         """
#         Returns self's name

#         """
#         return self.name


# me = Person("Michael Guttag")
# him = Person("Barack Hussein Obama")
# her = Person("Madonna")

# print(him.getLastName())
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))

# print(him.getName(), "is", him.getAge(), "days old")

# pList = [me, him, her]

# for p in pList:
#     print(p)
    
# pList.sort()
# print()

# for p in pList:
#     print(p)



###
# Slide
###

###
# Example: Simple co-ordinate class
###

# class Coordinate(object):
#     """
#     A co-ordinate made up of x and y value
#     """
    
#     def __init__(self, x, y):
#         """
#         Sets the x and y values.

#         """
#         self.x = x
#         self.y = y
    
#     def distance(self, other):
#         """
#         Returns the eucledian distance between two points

#         """
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
        
#         return (x_diff_sq + y_diff_sq)**0.5
    
#     def __str__(self):
#         """
#         Return a string representaion of self

#         """
#         return "<" + str(self.x) + ", " + str(self.y) + ">"
    
    
    

# c = Coordinate(3, 4)
# origin = Coordinate(0, 0)
# print(c.x, origin.x)

# print(c.distance(origin))
# print(origin.distance(c))
# print(c)
# print(type(c))

# print(type(Coordinate))
# print(isinstance(c, Coordinate))


###
# Example: Fraction
###

# class Fraction(object):
#     """
#     A number represented as fraction
#     """
    
#     def __init__(self, num, denum):
#         """
#         num and denum are integers.

#         """
#         assert type(num) == int and type(denum) == int, "ints not used"
        
#         self.num = num
#         self.denum = denum
        
#     def __str__(self):
#         """
#         Returns a string rperesentation of self

#         """
#         return str(self.num) + "/" + str(self.denum)
    
#     def __add__(self, other):
#         """
#         Returns a new fraction representing the addition

#         """
        
#         top = self.num * other.denum + self.denum * other.num
#         bottom = self.denum * other.denum
        
#         return Fraction(top, bottom)
    
#     def __sub__(self, other):
#         """
#         Returns a new fraction representing the subtraction

#         """
        
#         top = self.num * other.denum - self.denum * other.num
#         bottom = self.denum * other.denum
        
#         return Fraction(top, bottom)
    
#     def __float__(self):
#         """
#         Returns a float representation of self.

#         """
#         return self.num / self.denum
    
#     def inverse(self):
#         """
#         Returns a new fraction representing 1/self

#         """
#         return Fraction(self.denum, self.num)

# a = Fraction(1, 2)
# b = Fraction(3, 4)
# c = a + b
# print(c)

# print(float(c))
# print(b.inverse())
# print(float(b.inverse()))








