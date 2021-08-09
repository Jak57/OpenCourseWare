# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:43:33 2021

@author: jakir
"""
import numpy
# Calculating x^y

# Have to convert string to int
# X: 2, y: 3
x = int(input("Enter number x: ")) 
y = int(input("Enter number y: "))

# Can only concatenate string with string
# So, have to convert int to string
print("X**y = " + str(x**y))

# log2(x) calculates 2 base logarithm
z = numpy.log2(x)
print("log(x) = " + str(z))
