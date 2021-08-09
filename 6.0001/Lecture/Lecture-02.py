# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 17:22:26 2021

@author: jakir
"""

#####
# Example: Conditional
#####


# x = 2
# if x%2 == 0:
#     print("X is even")
# else:
#     print("X is odd")
# print("Done with conditional!")


####
# Example: Nested if
####

# x = int(input("Enter a number: "))

# if x%2 == 0:
#     if x%3 == 0:
#         print("Divisible by 2 and 3")
#     else:
#         print("Divisible by 2 but not 3")
# elif x%3 == 0:
#     print("Divisible by 3 but not 2")


# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))

# if x<y and x<z:
#     print("x is least")
# elif y<z:
#     print("y is least")
# else:
#     print("z is least")


####
# Finger Exercise
####

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))

# if x%2 == 1 or y%2 == 1 or z%2 == 1:
#     largest = 0
#     if x%2 == 1:
#         largest = max(largest, x)
#     if y%2 == 1:
#         largest = max(largest, y)
#     if z%2 == 1:
#         largest = max(largest, z)
    
#     print("Largest odd number: ", largest)
# else:
#     print("No odd number present!")




####
# Example: Iteration - Suare of a number
####

# x = -5
# if x<0:
#     x = abs(x)
    
# sum = 0
# itersLeft = x
# # itersLeft = abs(x) # In case we get a negative number

# while itersLeft != 0:
#     sum += x
#     itersLeft -= 1

# print(str(x) + "*" + str(x) + " = " + str(sum))



###
# Example: Finger Exercise
###

# numXs = int(input("How many time should I print the letter X? "))
# toPrint = ''

# while numXs != 0:
#     toPrint += 'X'
#     numXs -= 1

# print(toPrint)



###
# Example: Find a positive number that
# is divisible by both 11 and 12
###

# n = 1;

# while True:
#     if n%11 == 0 and n%12 == 0:
#         break
#     n += 1

# print(n , "is divisible by 11 and 12")



###
# Example: Finger Exercise
###

# itersLeft = 0
# ans = 0

# while itersLeft < 10:
#     n = int(input("Enter a number: "))
#     if n%2 == 1:
#         ans = max(ans, n)
#     itersLeft += 1

# if ans == 0:
#     print("No odd number found")
# else:
#     print("Maximum odd number is ", ans)




###
# Example: for loop
###

# x = 4
# for i in range(0, x):
#     print(i)
#     x = 5


# x = 4
# for i in range(x):
#     # inner range is evaluated each iteration of outer loop
#     for j in range(x):
#         print(j)
#         x = 7


###
# Example: Iterate through a string
###

# total = 0
# for i in '12345678':
#     total += int(i)
# print(total)



###
#Example: Finger Exercise
###

# s = '1.23, 2.4, 3.123'

# number = ''
# sum = 0.0
# for i in s:
    
#     if i == ',':
#         sum += float(number)
#         number = ''
#     elif i == ' ':
#         continue
#     else:
#         number += i

# sum += float(number)
# print("Sum:", sum)


####
# Slide
####


###
# Example: string
###

# name  = 'ana'
# greet = 'hi' + name
# print(greet)

# greet = 'hi' + ' ' + name
# print(greet)

# silly = 'hi' + (' ' + name)*3
# print(silly)



###
# Example: output
###

# x = 1
# x_str = str(x)
# print("My fav num is", x, ".", "x=", x)
# print("My fav num is " + x_str + " . " "x= " + x_str)
# print("My fav num is", x_str + "." + "x=", x)



###
# Example: input
###

# text = input("Type in something... ")
# print(text)
# print(5*text)

# num = int(input("Type in something... "))
# print(5*num)


###
# Example: Comparison
###

# pset_time = 15
# sleep_time = 8
# print(sleep_time > pset_time)

# derive = True
# drink = False
# both = derive and drink
# print(both)


###
# Example: Conditionals and Branching
###

# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))

# if x == y:
#     print("x is same as y")
#     if y != 0:
#         print("Therefore x/y is ", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")

# print("thanks!")


###
# Example: while loop
###

# dir = input("You are in the lost forest.\n********\n********\n  :) \n********\n********\nGo left or right?\n")
# while dir == "right" or dir == "Right":
#     dir = input("You are in the lost forest.\n********\n********\n  :( \n********\n********\nGo left or right?\n")

# print("You are out of the forest")



# n = 0
# while n < 5:
#     print(n)
#     n += 1



###
# Example: for loop
###

# for n in range(5):
#     print(n)

# mySum = 0
# for n in range(7, 10):
#     mySum += n
# print(mySum)


# mySum = 0
# for n in range(5, 11, 2):
#     mySum += n
# print(mySum)

# mySum = 0
# for i in range(5, 11, 2):
#     mySum += i
#     if mySum == 5:
#         break
#         mySum += 1
# print(mySum)




