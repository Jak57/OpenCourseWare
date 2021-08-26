# Problem Set 2, hangman.py
# Name: Jakir
# Collaborators:
# Time spent: 3 Days

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    # n: int
    n = len(secret_word)
    # count: int
    count = 0
    
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                count += 1
    
    if count == n:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    # guessed_word: string
    guessed_word = ""
    # flag: int
    flag = 0
    
    for char1 in secret_word:
        flag = 0
        for char2 in letters_guessed:
            if char1 == char2:
                guessed_word += char1
                flag += 1
                
        if flag == 0:
            guessed_word += "_ "
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    
    # available_letters: string
    available_letters = ""
    
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
    
    return available_letters

def isVowel(ch):
    """
    

    Parameters
    ----------
    ch : char in lowercase

    Returns: True if the char is vowel and false otherwise
    -------
    

    """
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else:
        return False


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # n: int
    n = len(secret_word)
    # numGuesses: int
    numGuesses = 6
    # warning: int
    warning = 3
    # letters_guessed: list of guessed letters
    letters_guessed = []
    # guessed_word: string
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    # unique_letter: int
    unique_letter = 0
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", n ,"letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    
    while not is_word_guessed(secret_word, letters_guessed) and numGuesses > 0:
        
        print("You have", numGuesses, "guesses left.")
        # available_letters: string
        available_letters = get_available_letters(letters_guessed)
        
        print("Available letters:", available_letters)
        # guessed_letter: char
        guessed_letter = input("Please guess a letter: ")
        
        if str.isalpha(guessed_letter):
            
            str.lower(guessed_letter)
            
            if guessed_letter not in letters_guessed:
                letters_guessed.append(guessed_letter)
                
                if guessed_letter in secret_word:

                    guessed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", guessed_word)
                    unique_letter += 1
                else:
                    if isVowel(guessed_letter):
                        numGuesses -= 2
                    else:
                        numGuesses -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
                
            else:
                if warning >= 1:
                    warning -= 1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left:", guessed_word)
                else:
                    numGuesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", guessed_word)
        else:
            if warning >= 1:
                warning -= 1
                print("Oops! That is not a valid letter. You have", warning ,"warnings left:", guessed_word)
            else:
                numGuesses -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", guessed_word)
                
        print("-------------")
        
     
    
    if secret_word == guessed_word:
        # guess_remaining: int
        guess_remaining = numGuesses
        # total_score: int
        total_score = unique_letter * guess_remaining
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ". ")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # word_without_space: string
    word_without_space = ""
    # flag: int
    flag = 0
    
    for char in my_word:
        if char != " ":
            word_without_space += char
    
    if len(other_word) == len(word_without_space):
        
        for i in range(len(word_without_space)):
            if word_without_space[i] != "_":
                if word_without_space[i] != other_word[i]:
                    flag += 1
        if flag == 0:
            return True
        
    return False
        


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass

    # count: int
    count = 0
    # matched_word_list: list
    matched_word_list = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            matched_word_list.append(other_word)
            count += 1
            
    if count > 0:
        print("Possible word matches are:")
        for other_word in matched_word_list:
            print(other_word + " ", end = '')
        print("")
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    n = len(secret_word)
    numGuesses = 6
    warning = 3
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    unique_letter = 0
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", n ,"letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    
    while not is_word_guessed(secret_word, letters_guessed) and numGuesses > 0:
        
        print("You have", numGuesses, "guesses left.")
        available_letters = get_available_letters(letters_guessed)
        
        print("Available letters:", available_letters)
        guessed_letter = input("Please guess a letter: ")
        
        if str.isalpha(guessed_letter):
            
            str.lower(guessed_letter)
            
            if guessed_letter not in letters_guessed:
                letters_guessed.append(guessed_letter)
                
                if guessed_letter in secret_word:

                    guessed_word = get_guessed_word(secret_word, letters_guessed)
                    print("Good guess:", guessed_word)
                    unique_letter += 1
                else:
                    if isVowel(guessed_letter):
                        numGuesses -= 2
                    else:
                        numGuesses -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
                
            else:
                if warning >= 1:
                    warning -= 1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left:", guessed_word)
                else:
                    numGuesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", guessed_word)
        elif guessed_letter == "*":
            show_possible_matches(guessed_word)
        else:
            if warning >= 1:
                warning -= 1
                print("Oops! That is not a valid letter. You have", warning ,"warnings left:", guessed_word)
            else:
                numGuesses -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", guessed_word)
                
        print("-------------")
        
     
    
    if secret_word == guessed_word:
        guess_remaining = numGuesses
        total_score = unique_letter * guess_remaining
        print("Congratulations, you won!")
        print("Your total score for this game is:", total_score)
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ". ")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)




###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
