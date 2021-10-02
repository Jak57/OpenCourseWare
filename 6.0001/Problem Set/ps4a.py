# Problem Set 4A
# Name: Jakir Hasan
# Collaborators:
# Time Spent: 1:30

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # L: list
    L = []
   
    if len(sequence) == 1:
        L.append(sequence)
        return L
    else:
        first_letter = sequence[0]
        permutation_list = get_permutations(sequence[1:])
        
        # temp_list (list): stores all possible permutations
        temp_list = []
        
        for word in permutation_list:
            for i in range(len(word)+1):
                new_word = word[:i] + first_letter + word[i:]
                temp_list.append(new_word)
                     
        return temp_list

if __name__ == '__main__':
    # #EXAMPLE
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    
    # # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)

    example_input = 'ox'
    print('Input:', example_input)
    print('Expected Output:', ['ox', 'xo'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['hen', 'ehn', 'enh', 'hne', 'nhe', 'neh'])
    print('Actual Output:', get_permutations(example_input))
    print()
    
    example_input = 'fox'
    print('Input:', example_input)
    print('Expected Output:', ['fox', 'ofx', 'oxf', 'fxo', 'xfo', 'xof'])
    print('Actual Output:', get_permutations(example_input))





