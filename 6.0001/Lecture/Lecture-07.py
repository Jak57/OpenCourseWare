# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:05:14 2021

@author: jakir
"""

###
# Book: Exceptions and Assertions
###

###
# Example: Handling Exceptions
###

# numSuccesses = 8
# numFailures = 0

# successFailureRatio = numSuccesses/numFailures
# print('The Success/Failure ratio is', successFailureRatio)
# print('Now there')

# numSuccesses = 8
# numFailures = 0

# try:
#     successFailureRatio = numSuccesses/numFailures
#     print('The Success/Failure ratio is', successFailureRatio)
# except:
#     print('No failures, so the Success/Failure ratio is undefined')
# print('Now here')



###
# Example: User input
###


# val = int(input('Enter an integer: '))
# print('The square of the number you entered is', val**2)


# while True:
#     val = input('Enter an integer: ')
#     try:
#         val = int(val)
#         print('The square of the number you entered is', val**2)
#         break
#     except:
#         print(val, 'is not an integer')


# def readInt():
    
#     while True:
#         val = input('Enter an integer: ')
#         try:
#             return int(val)
#         except:
#             print(val, 'is not an integer')

# n = readInt()
# print(n)


# ******* #
### Reading any type of user input

# def readVal(valType, requestMsg, errorMsg):
   
#     while True:
#         val = input(requestMsg + ' ')
#         try:
#             return valType(val)
#         except ValueError:
#             print(val, errorMsg)

# print(readVal(int, 'Enter an integer:', 'is not an integer'))


###
# Example: Finger Exercise
###

# def findAnEven(L):
#     """
#     Assumes L is an int. Return the first even number in L.
#     Raise an exception if L doesn't contain an even number.

#     """
#     for num in L:
#         if num%2 == 0:
#             return num
        
#     raise ValueError('does not contain an even number')

# print(findAnEven([1, 5, 3]))


###
# Example: Raise Exception
###

# def getRatios(vect1, vect2):
#     """
#     Assumes vect1 and vect2 are equal length lists of numbers.
#     Returns: a list of meaningful values of vect1[i]/vect2[i]

#     """
#     ratios = []
#     for index in range(len(vect1)):
#         try:
#             ratios.append(vect1[index]/vect2[index])
#         except ZeroDivisionError:
#             ratios.append(float('nan')) # nan = Not a Number
#         except:
#             raise ValueError('getRatios called with bad arguments')

#     return ratios

# try:
#     print(getRatios([1, 2, 7, 6], [1, 2, 0, 3]))
#     print(getRatios([], []))
#     print(getRatios([1, 2], [3]))
# except ValueError as msg:
#     print(msg)
    

# ******** #
# Without try-except block

# def getRatios(vect1, vect2):
#     ratios = []
    
#     if len(vect1) != len(vect2):
#         raise ValueError('getRatios called with bad arguments')
    
#     for index in range(len(vect1)):
#         vect1_elem = vect1[index]
#         vect2_elem = vect2[index]
        
#         if type(vect1_elem) not in (int, float) or type(vect2_elem) not in (int, float):
#             raise ValueError('getRatios called with bad arguments')
            
#         if vect2_elem == 0:
#             ratios.append(float('nan'))
#         else:
#             ratios.append(vect1_elem/vect2_elem)

#     return ratios

# try:
#     print(getRatios([1, 2, 7, 6], [1, 2, 0, 3]))
#     print(getRatios([], []))
#     print(getRatios([1, 2], [3]))
# except ValueError as msg:
#     print(msg)


###
# Example: Grade
###

# def getGrades(fname):
    
#     try:
#         gradesFile = open(fname, 'r') # open file for reading
#     except IOError:
#         raise ValueError('getGrades could not open ' + fname)

#     grades = []
#     for line in gradesFile:
#         try:
#             grades.append(float(line))
#         except:
#             raise ValueError('Unable to convert line to float')
#     return grades

# try:
#     grades = getGrades('quiz1grades.txt')
#     grades.sort()
#     median = grades[len(grades)//2]
#     print('Median grade is', median)
# except ValueError as errorMsg:
#     print('whoops.', errorMsg)


##########
# Slides
#########

###
# Example: Flow 
###

# try:
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b =", a/b)
#     print("a+b =", a+b)
# except ValueError:
#     print("Could not convert to an integer.")
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# except:
#     print("Something went very wrong.")


###
# Example: Exception and List
###

# # without exception
# def average(grades):
#     return sum(grades)/len(grades)

# with exception
# def average(grades):
#     try:
#         return sum(grades)/len(grades)
#     except ZeroDivisionError:
#         print("warning! no grade data.")
#         return 0.0

# with assert
# def average(grades):
#     """
    

#     Parameters
#     ----------
#     grades : list of number
        

#     Returns average of the numbers
#     -------
    

#     """
#     assert not len(grades) == 0, "warning: no grade data"
#     return sum(grades)/len(grades)

# def get_stats(class_list):
#     """
    

#     Parameters
#     ----------
#     class_list : list
        

#     Returns
#     -------
#     new_stats : list
       

#     """
#     new_stats = []
#     for  person in class_list:
#         new_stats.append([person[0], person[1], average(person[1])])

#     return new_stats

# test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
#               [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
#               [['captain', 'america'], [80.0, 70.0, 96.0]],
#               [['deadpool'], []]]

# new_stats = get_stats(test_grades)
# print(new_stats)



