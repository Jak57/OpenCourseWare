# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:53:51 2021

@author: jakir
"""

###
# Book
###

###
# Example: Cube root of a perfect cube
###

# num = int(input("Enter an integer: "))
# ans = 0

# while ans**3 < abs(num):
#     ans += 1
    
# if ans**3 != abs(num):
#     print(num, "is not a perfect cube")
# else:
#     if num < 0:
#         ans = -ans
#     print("Cube root of", num , "is", ans)


### Fun
# maxVal = int(input("Enter a positive integer: "))
# i = 0

# while i<maxVal:
#     i += 1
# print(i)



###
# Finger exercise
###

# n = int(input("Enter a positive integer: "))

# pow = 1
# cnt = 0

# while pow<6:
#     for root in range(n): # root can't be equal to n and pow can't be equal to 1
        
#         if root**pow == n:
#             print("root:", root, "and pow:", pow)
#             cnt += 1
#             break
#     if cnt > 0:
#         break
#     pow += 1
        
# if cnt == 0:
#     print("Can't find root and pow")



###
# Example: Approximation of square root
###

#x = int(input("Enter a positive integer: "))
# x = 123456
# epsilon = 0.01
# step = epsilon**3
# numGuesses = 0
# ans = 0.0

# while abs(ans**2 - x) >= epsilon and ans**2 <= x:
#     ans += step
#     numGuesses += 1

# print("Total guesses: ", numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print("Failed to find square root")
# else:
#     print("Approximate value of square root is", ans)



###
# Example: Bisection search
###

# x = 25
# epsilon = 0.01
# low = 0.0
# high = max(1.0, x)
# ans = (low + high)/2.0
# numGuesses = 0

# while abs(ans**2 - x) >= epsilon:
#     print("low = ", low, "high = ", high, "ans = ", ans)
    
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans

#     ans = (low + high)/2.0
#     numGuesses += 1

# print("numGuesses = ", numGuesses)
# print(ans, "is close to square root of", x)


###
# Finger Exercise
###

# If we put x = -25, the above code will fall in a infinite loop

###
# Finger Exercise: Cube root of any positive or negative number
###

# x = int(input("Enter an integer: "))
# cnt = 0
# if x < 0:
#     x = -x
#     cnt += 1
    
# epsilon = 0.01
# low = 0.0
# high = max(1.0, x)
# ans = (low + high)/2.0
# numGuesses = 0

# while abs(ans**3 - x) >= epsilon:
#     print("low = ", low, "high = ", high, "ans = ", ans)
    
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans

#     ans = (low + high)/2.0
#     numGuesses += 1

# print("numGuesses = ", numGuesses)
# if cnt == 0:
#     print(ans, "is close to cube root of", x)
# else:
#     print(-ans, "is close to cube root of", -x)
    
    
# x = -64
    
# epsilon = 0.01
# if x < 0:
#     low = x
#     high = 0.0
# else:
#     low = 0.0
#     high = max(1.0, x)
# ans = (low + high)/2.0
# numGuesses = 0

# while abs(ans**3 - x) >= epsilon:
#     print("low = ", low, "high = ", high, "ans = ", ans)
    
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans

#     ans = (low + high)/2.0
#     numGuesses += 1

# print("numGuesses = ", numGuesses)
# print(ans, "is close to cube root of", x)


###
# Example: float
###

# x = 0.0
# for i in range(10):
#     x += 0.1

# if x == 1.0:
#     print(x, "= 1.0")
# else:
#     print(x, "is not 1.0")
    


###
# Slides
###

###
# Example: loop over string
###

# s = "abcdefghij"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")

# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")


###
# Example: Robots Cheerleaders
###

# an_words = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# for char in word:
#     if char in an_words:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)

# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")



###
# Example: Common letters
###

# s1 = "mit u rock"
# s2 = "i rule mit"

# if len(s1) == len(s2):
#     for char1 in s1:
#         for char2 in s2:
#             if char1 == char2 and char1 != ' ':
#                 print("Common letter", char1)
#                 break


###
# Example: Cube root finding by Guess and Check
###

# cube = 8
# for guess in range(cube+1):
#     if guess**3 == cube:
#         print("Cube root of", cube, "is", guess)
        

# cube = int(input('Enter an integer: '))
# flag = 0
# if cube < 0:
#     cube = -cube
#     flag += 1

# for guess in range(cube+1):
#     if guess**3 >= cube:
#         break

# if flag > 0:
#     cube = -cube
#     guess = -guess
    
# if guess**3 != cube:
#     print(cube, "is not a perfect cube")
# else:
#     print("Cube root of", cube, "is", guess)



# cube = int(input('Enter an integer: '))

# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
    
# if guess**3 != abs(cube):
#     print(cube, "is not a perfect cube")
# else:
#     if cube < 0:
#         guess = -guess
#     print("Cube root of", cube, "is", guess)


###
# Example: Approximate solution of cube root
###

# cube = 27
# epsilon = 0.01
# guess = 0.0
# increment = 0.0001
# numGuesses = 0

# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     numGuesses += 1

# print("numGuesses:", numGuesses)
# if abs(guess**3 - cube) >= epsilon:
#     print("Failed to find cube root of", guess)
# else:
#     print(guess, "is close to the cube root of", cube)


###
# Example: Bisection search
###

# cube = 10000
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = cube
# guess = (low + high)/2.0

# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     numGuesses += 1
#     guess = (low + high)/2.0
    
# print("numGuesses:", numGuesses)
# print(guess,"is close to the cube root of", cube)
        






