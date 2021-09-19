# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:40:02 2021

@author: jakir
"""

###
# Example: Factorial
###

# def factI(n): # Iterative
#     """
    

#     Parameters
#     ----------
#     n : int 
#         n > 0

#     Returns
#     -------
#     result : int
#         n!

#     """
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result

# print(factI(7))


# Recursive

# def factR(n):
#     """
#     Assumes n an int > 0
#     Returns n!

#     """
#     if n == 1:
#         return 1
#     else:
#         return n * factR(n-1)

# print(factR(10))

###
# Example: Fibonacci sequence
###

# def fib(n):
#     """
#     Assumes n an int > 0
#     Returns fibonacci of n

#     """
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# def testFib(n):
#     for i in range(n+1):
#         print("fib of", i, "=", fib(i))

# testFib(10)


###
# Example: Palindrome
###

# def isPalindrome(s):
#     """
#     Assumes s is a string
#     Returns True if s is a palindrome and False oterwise.
#     Non-letters and capitalizations are ignored.

#     """
#     def toChars(s):
#         s = s.lower()
#         letters = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 letters += c
#         return letters

#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
    
#     return isPal(toChars(s))

# print(isPalindrome("Abc dcba"))
# # print(isPalindrome("Abc dcbaa"))


# Viualization

# def isPalindrome(s):
#     """
#     Assumes s is a string
#     Returns True if s is a palindrome and False oterwise.
#     Non-letters and capitalizations are ignored.

#     """
#     def toChars(s):
#         s = s.lower()
#         letters = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 letters += c
#         return letters

#     def isPal(s):
#         print("  isPal called with", s)
#         if len(s) <= 1:
#             print("  About to return True from base case")
#             return True
#         else:      
#             answer = s[0] == s[-1] and isPal(s[1:-1])
#             print("  About to return", answer, "for", s)
#             return answer
    
#     return isPal(toChars(s))

# def testPalindrome():
#     print("Try dogGod")
#     print(isPalindrome("dogGod"))
#     print("Try doGood")
#     print(isPalindrome("doGood"))

# testPalindrome()

###
# Example: Dictionaries
###

# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr': 4, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr'}
# print("The third month is", monthNumbers[3])
# dist = monthNumbers['Apr'] - monthNumbers['Jan']
# print("Apr and Jan are", dist, "months apart")


###
# Example: Translation
###

# EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je', 
#         'eat':'mange', 'drink':'bois', 'John':'Jean', 'friends':'amis',
#         'and':'et', 'of':'du', 'red':'rouge'}
# FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 
#         'mange':'eat', 'bois':'drink', 'Jean':'John', 'amis':'friends',
#         'et':'and', 'du':'of', 'rouge':'red'}

# dicts = {'English to French':EtoF, 'French to English':FtoE}

# def translateWord(word, dictionary):
    
#     if word in dictionary.keys():
#         return dictionary[word]
#     elif word != '':
#         return '"' + word + '"'
#     return word

# def translate(phrase, dicts, direction):
#     UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     LCLetters = 'abcdefghijklmnopqrstuvwxyz'
#     letters = UCLetters + LCLetters
#     dictionary = dicts[direction]
    
    
#     translation = ''
#     word = ''
    
#     for c in phrase:
#         if c in letters:
#             word = word + c
#         else:
#             translation = translation + translateWord(word, dictionary) + c
#             word = ''
#     return translation + ' ' + translateWord(word, dictionary)

# print(translate('I drink good red wine, and eat bread.', dicts, 'English to French'))
# print(translate('Je bois du vin rouge.', dicts, 'French to English'))

# FtoE['bois'] = 'wood'
# print(translate('Je bois du vin rouge.', dicts, 'French to English'))


###
# Example: Order of retrieval
###

# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr': 4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}

# keys = []
# for e in monthNumbers:
#     keys.append(str(e))
    
# print(keys)
# print(monthNumbers.keys())
# monthNumbers['July'] = '7'

# print(monthNumbers.keys())
# print(monthNumbers.values())
# print(list(monthNumbers.values()))


###
# Slide: Dictionary
###

###
# Example: Storing student info using lists
###

# def get_grade(student, name_list, grade_list, course_list):
#     i = name_list.index(student)
#     grade = grade_list[i]
#     course = course_list[i]
#     return (grade, course)

# names = ['Ana', 'John', 'Denise', 'Katy']
# grades = ['B', 'A+', 'A', 'A']
# course = [2.00, 6.0001, 20.002, 9.01]

# (grade, course) = get_grade('Katy', names, grades, course)
# print(grade, course)



###
# Example: Dictionary
###

# my_dict = {}
# grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}
# print(grades['John'])
# # print(grades['Sylvan']) # KeyError
# grades['Sylvan'] = 'A'
# print(grades['Sylvan'])

# d = {4:{1:0}, (1, 3):"twelve", 'const':[3.14, 2.7, 8.44]}
# print(d)


###
# Example: Beatles
###

# def lyrics_to_frequencies(lyrics):
#     """

#     Parameters
#     lyrics: list

#     Returns a dictionary of (word -> no. of time that word
#     occurs in lyrics)
#     -------
#     myDict : Dict   

#     """
#     myDict = {}
    
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
    
#     return myDict

# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
# 'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

# 'you', 'think', "you've", 'lost', 'your', 'love',
# 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
# "it's", 'you', "she's", 'thinking', 'of',
# 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'she', 'said', 'you', 'hurt', 'her', 'so',
# 'she', 'almost', 'lost', 'her', 'mind',
# 'and', 'now', 'she', 'says', 'she', 'knows',
# "you're", 'not', 'the', 'hurting', 'kind',

# 'she', 'says', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',

# 'you', 'know', "it's", 'up', 'to', 'you',
# 'i', 'think', "it's", 'only', 'fair',
# 'pride', 'can', 'hurt', 'you', 'too',
# 'pologize', 'to', 'her',

# 'Because', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
# 'Yes', 'she', 'loves', 'you',
# 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

# 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'with', 'a', 'love', 'like', 'that',
# 'you', 'know', 'you', 'should', 'be', 'glad',
# 'yeah', 'yeah', 'yeah',
# 'yeah', 'yeah', 'yeah', 'yeah'
# ]


# myDict = lyrics_to_frequencies(she_loves_you)


# def most_common_words(freqs):
    
#     """
#     freqs: dict (str -> int)
#     (word -> no. of times that word occur in the song)
    
#     Returns a tuple of the list of words that occur most times and the 
#     number of times
    
#     common_words: list
#     best: int
    
#     """
#     values = freqs.values()
#     best = max(values)
    
#     common_words = []
#     for word in freqs:
#         if freqs[word] == best:
#             common_words.append(word)

#     return (common_words, best)



# def words_often(frequency, minTimes):
#     """
#     frequency: dict (str -> int)
#     minTimes: int

#     Returns a list of tuples (list -> int) where words occur minimum 5 times
#     -------
#     result : list
        

#     """
#     result = []
#     done = False
    
#     while not done:
#         temp = most_common_words(frequency)
        
#         if temp[1] >= minTimes:
#             result.append(temp)
            
#             for word in temp[0]:
#                 del(frequency[word])
#         else:
#             done = True
    
#     return result

# print(words_often(myDict, 5))


###
# Example: Fibonacci recursive code
###

### Inefficient version

# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(34))



###
# Example: Fibonacci with dictionary
###

# def fib_efficient(n, d):
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#         d[n] = ans
#         return d[n]

# d = {1:1, 2:2}

# print(fib_efficient(34, d))

### End of dictionary


### First part of slide

###
# Example: Multiplication
###

# Iterative solution

# def mult_iter(a, b):
#     result = 0
    
#     while b > 0:
#         result += a
#         b -= 1
    
#     return result

# print(mult_iter(3, 9))



### Recursive solution

# def mult(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + mult(a, b-1)

# print(mult(4, 9))


###
# Example: Factorial
###

### Iterative approach

# def fact_iter(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(fact_iter(4))


### Recursive approach

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))


###
# Example: Towers of Hanoi
###

# def printMove(fr, to):
#     print('Move from', fr, 'to', to)

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
#     else:
#         Towers(n-1, fr, spare, to)
#         printMove(fr, to)
#         Towers(n-1, spare, to, fr)

# Towers(4, 'P1', 'P2', 'P3')
