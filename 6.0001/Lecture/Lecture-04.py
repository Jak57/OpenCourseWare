# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:02:12 2021

@author: jakir
"""


###
# Book
###


###
# Finger exercise
###

# def isIn(s1, s2):
#     if (s1 in s2) or (s2 in s1):
#         return True
#     else:
#         return False
    
# s1 = "jakir"
# s2 = "hasanejakirlee"

# print(isIn(s1, s2))


###
# Example: keyWord argument
###

# def printName(firstName, lastName, reverse = True):
#     if reverse:
#         print(lastName + ", " + firstName)
#     else:
#         print(firstName, lastName)

# # Positional argument must be before keyword arguments
# printName("Olga", "Punchmajerova", False)
# printName("Olga", "Punchmajerova", reverse = False)
# printName("Olga", lastName = "Punchmajerova", reverse = False)
# printName(firstName = "Olga", lastName="Punchmajerova", reverse=False)
# printName(lastName="Punchmajerova", firstName = "Olga", reverse = False)
# printName("Olga", "Punchmajerova")


###
# Example: Scope
###

# def f(x):
#     y = 1
#     x = x + y
#     print("x =", x)
#     return x

# x = 3
# y = 2
# z = f(x)

# print("z =", z)
# print("x =", x)
# print("y =", y)


###
# Example: Nested scope
###

# def f(x):
#     def g():
#         x = "abc"
#         print("x =", x)
        
#     def h():
#         z = x
#         print("z =", z)
    
#     x = x + 1
#     print("x =", x)
#     g()
#     h()
#     print("x =", x)
#     return g

# x = 3
# z = f(x)
# print("x =", x)
# print("z =", z)
# z()
    


# def f():
#     print(x)

# def g():
#     print(x) # local variable can't be accessed before assignment
#     x = 1
    
# x = 3
# f()
# x = 3
# g()



###
# Example: Finding root
###

# def findRoot(x, power, epsilon):
#     """
#     Assumes x and power int or float, power an int, epsilon > 0 and power >= 1
#     Return float y such that y**power is within epsilon of x.
#     If such a float does not exist, it returns None
    
#     """
#     if x < 0 and power%2 == 0:
#         return None # Negative number has no even powered root
    
#     low = min(-1.0, x)
#     high = max(1.0, x)
#     ans = (low + high)/2.0
    
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (low + high)/2.0
#     return ans
    
    
# def testFindRoot():
#     epsilon = 0.0001
#     for x in [0.25, -0.25, 2, -2, 8, -8]:
        
#         for power in range(1, 4):
#             print("Testing x =", str(x), "and power =", power)
#             result = findRoot(x, power, epsilon)
#             if result == None:
#                 print("   No root")
#             else:
#                 print("   ", result**power, "~=", x)
    
    
# testFindRoot() 
    
    
    
###
# Slide
###

###
# Example: Combinations of print and return
###

# def is_even_with_return(i):
#     """

#     Parameters
#     ----------
#     i : a positive integer

#     Returns True if i is a even number and False otherwise
    
#     """
    
#     print("with return")
#     remainder = i % 2
#     return remainder == 0

# is_even_with_return(3)
# print(is_even_with_return(3))

# def is_even_without_return(i):
#     """
    

#     Parameters
#     ----------
#     i : a positive integer
#     Does not return anything
#     -------
#     None.

#     """
#     print("without return")
#     remainder = i % 2
    
# is_even_without_return(4)
# print(is_even_without_return(4))



### Simple is_even function
# def is_even(i):
#     """

#     Parameters
#     ----------
#     i : a positive integer

#     Returns True if i is a even number and False otherwise
    
#     """
    
#     remainder = i % 2
#     return remainder == 0

# # Use the is_even function later in this code
# print("All numbers between 0 and 20: even or odd")
# for i in range(20):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")


###
# Example: Scope
###

# def f(x):
#     x = x + 1
#     print("in f(x): x =", x)
#     return x

# x = 3
# z = f(x)
# print("z =", z)


###
# Example: Functions as argument
###

def func_a():
    print("inside func_a")

def func_b(y):
    print("inside func_b")
    return y

def func_c(z):
    print("inside func_c")
    return z()

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


###
# Example: Scope
###

# def f(y):
#     x = 1
#     x += 1
#     print(x)

# x = 5
# f(x)
# print("x =", x)

# def g(y):
#     print(x)
#     print(x+1)

# x = 3
# g(x)
# print(x)

# def h(y):
#     x = x + 1 # UnboundLocalError
#     print(x)

# x = 5
# h(x)
# print(x)


# def g(x):
#     def h():
#         x = "abc"
#         print("h: x =", x)
        
#     x = x + 1
#     print("g: x =", x)
#     h()
#     return x

# x = 3
# z = g(x)
# print("z =", z)




