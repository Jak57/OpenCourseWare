# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 19:28:47 2021

@author: jakir
"""

###
# Example: tupe
###

# t1 = ()
# t2 = (1, 'two', 3)
# print(t1)
# print(t2)

# t3 = (1)
# print(t3)
# # For representing tuple of single element, we have to add a comma
# t4 = (2,) 
# print(t4)

# # tuple can be indexed, concatenated and sliced
# t5 = ('a', 2)
# print(3*t5)
# t6 = (1, 2, 3)
# print(t6)
# # Can make tuple of tuple
# t7 = (t6, 3.25)
# print(t7)
# print(t6 + t7)
# print((t6 + t7)[3])
# print((t6 + t7)[2:5])



###
# Example: Iterate through a tuple
###

# def intersect(t1, t2):
#     """
    

#     Parameters
#     ----------
#     Assumes t1 and t2 are tuple and return a tuple
#     containing elements that are both in t1 and t2
#     -------

#     """
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
    
#     return result

# t1 = (1, 2, 3, 4)
# t2 = (2, 5, 1)
# print(intersect(t1, t2))



###
# Example: Multiple assignment
###

# def findExtremeDivisors(n1, n2):
#     """
#     Assumes n1 and n2 are ints
#     Returns a tuple of smallest common divisor > 1 and largest common divisor of n1 
#     and n2
#     If no common divisor returns (None, None)

#     """
#     minVal, maxVal = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             if minVal == None:
#                 minVal = i
#             maxVal = i
            
#     return (minVal, maxVal)
    
# minDivisor, maxDivisor = findExtremeDivisors(100, 200)
# print(minDivisor, maxDivisor)
    
    
    
###
# Example: list
###

# L = ['I did it all', 4, 'love'] 
# for i in range(len(L)):
#     print(L[i])
    
# Techs = ['MIT', 'caltech']  
# Ivys = ['Harvard', 'Yale', 'Brown']

# Univs = [Techs, Ivys]
# Univs1 = [['MIT', 'caltech'], ['Harvard', 'Yale', 'Brown']]

# print("Univs:", Univs)
# print("Univs1:", Univs1)
# # test value equality
# print(Univs == Univs1)
# # test object eqality    
# print(id(Univs) == id(Univs1))
# print("Id of Univs:", id(Univs))
# print("Id of Univs1:", id(Univs1))

# print("Id of Univs[0] and Univs[1]:", id(Univs[0]), id(Univs[1]))
# print("Id of Univs1[0] and Univs1[1]:", id(Univs1[0]), id(Univs1[1]))

# Techs.append("RPI")
# print("Univs:", Univs)
# print("Univs1:", Univs1)

# for e in Univs:
#     print("Univs contains", e)
#     print("  which contains")
#     for u in e:
#         print("    ", u)
    

# Techs.append(Ivys)
# print(Techs)


###
# Example: List operations
###

# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# L3 = L1 + L2 # + doesn't mutate list
# print("L3 =", L3)

# L1.extend(L2)
# print("L1 =", L1) # extend, append mutates list
# L1.append(L2)
# print("L1 =", L1)



###
# Example: Cloning
###

# def removeDups(L1, L2): # mutating list in loop creates problem
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
            
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups(L1, L2)
# print("L1 =", L1)

# def removeDups(L1, L2): # mutating list in loop creates problem
#     for e1 in L1[:]: # slicing can solve the problem of mutation
#         if e1 in L2:
#             L1.remove(e1)
            
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups(L1, L2)
# print("L1 =", L1)


###
# Example: Function as object
###
    

# def factR(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#     return ans

# def applyToEach(L, f):
#     """
#     Assumes L is list and f is function
#     Mutate L by replacing each element of e by f(e)

#     """
#     for i in range(len(L)):
#         L[i] = f(L[i])

# L = [1, -2, 3.33]
# print("L =", L)
# print("Apply abs to each element of L", L)
# applyToEach(L, abs)
# print("L =", L)

# print("Apply int to each element of L", L)
# applyToEach(L, int)
# print("L =", L)

# print("Apply factorial to each element of L", L)
# applyToEach(L, factR)
# print("L =", L)


###
# Example: map
###

# def factR(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#     return ans

# for i in map(factR, [1, 2, 3, 4]):
#     print(i)


# L1 = [1, 2, 3, 4]
# L2 = [4, 1, 7, 3]

# for i in map(min, L1, L2):
#     print(i)

###
# Example: lambda expression
###

# L = []
# for i in map(lambda x, y: x**y, [1, 2, 3, 4], [3, 2, 1, 0]):
#     L.append(i)
# print(L)


###
# String spliting
###

# print("My favorite professor--John G.--rocks".split(" "))
# print("My favorite professor--John G.--rocks".split("-"))
# print("My favorite professor--John G.--rocks".split("--"))


### Slide


###
# Example: Tuple
###

# te = ()
# t = (2, "mit", 4)
# print(t[0])
# print(te)
# t1 = (2, "mit", 4) + (5, 6)
# print(t1)
# print(t[1:2])
# print(t[1:3])

###
# Example: swap
###

# x = 3
# y = 4
# print("x:", x)
# print("y:", y)
# x, y = y, x
# print("x:", x)
# print("y:", y)


###
# Example: Return tuple
###

# def quotient_and_remainder(x, y):
#     quot = x//y
#     rem = x%y
#     return (quot, rem)

# quot, rem = quotient_and_remainder(5, 2)
# print(quot, rem)


###
# Example: iterating over tuple
###

# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
            
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
    
#     return (min_n, max_n, unique_words)

# (min_n, max_n, unique_words) = get_data(((4, "jak"), (5, "lee"), (1, "jak")))
# print(min_n, max_n, unique_words)

###
# Example: list
###

# a_list = []
# L = [2, 'a', 4, [1, 2]]
# print(len(L), L[0], L[2]+1, L[3])
# i = 2
# print(L[i-1])

# mutation
# L = [2, 1, 3]
# L[1] = 5
# print(L)

# total = 0
# for i in L:
#     total += i
# print(total)

# L.append(6)
# print(L)


###
# Example: list operation
###

# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# L3 = L1 + L2
# print(L3)
# L1.append([0, 6])
# print(L1)

# L1.append('a')
# print(L1)
# del(L1[3])
# print(L1)
# x = L1.pop()
# print(L1, x)

# L = [1, 2, 3, 4, 5, 5, 6, 2]
# L.remove(2)
# print(L)
# del(L[1])
# print(L)
# print(L.pop())

###
# Example: string to list and list to string
###

# s = "I<3 cs"
# L = list(s)
# print(L)
# L1 = s.split("<")
# print(L1)

# L = ['a', 'b', 'c']
# print(''.join(L))
# s2 = '_'.join(L)
# print(s2)

# L = [4, 3, 0, 9, 1]
# print(sorted(L))
# print(L)
# L.sort()
# print(L)
# L.reverse()
# print(L)


###
# Example: Aliasing
###

# a = 1
# b = a
# print(a, b)
# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

# Cloning list
# cool = ['red', 'yellow', 'green']
# chill = cool[:]
# chill.append('black')
# print(chill)
# print(cool)

###
# Example: Sorting
###


# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)

# cool = ['gray', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)

###
# Example: nested list
###

# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)

# print(brightcolors)
# hot.append('pink')
# print(hot)
# print(brightcolors)

###
# Example: Mutation and iteration
###

# def remove_dups(L1, L2):
#     for e in L1:
#         if e in L2:
#             L1.remove(e)
#     return L1

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# print(remove_dups(L1, L2)) # don't remove duplicate properly


# def remove_dups(L1, L2):
#     L1_copy = L1[:]
#     for e in L1_copy:
#         if e in L2:
#             L1.remove(e)
#     return L1

# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# print(remove_dups(L1, L2))
