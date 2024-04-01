from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # split the string into a list of strings
    # use the map function to convert each string in the list to an int
    # use the sorted function to sort the list of ints
    # use the join function to convert the list of ints to a string
    # return the string
    pass


def check_sentence_spelling(sentence: str) -> bool:
    """ Input is a string of one or more words.
    Return True if every word in the string is spelled correctly using the dictionary found in the code
    >>> check_sentence_spelling('The red and the black made white')
    True
    >>> check_sentence_spelling('The red and the black made whilte')
    False
    """
    # create a dictionary of words from the imported words list
    # use the split function to split the sentence into a list of words
    # use the map function to convert each word in the list to lowercase
    # use the list comprehension to evaluate each word in the list against the dictionary
    # return the result
    pass


def find_word(sentence: str, word: str) -> bool:
    """ Input is a string of one or more words and a word to search for.
    Return True if the word is found in the string using the find function
    >>> find_word('The red and the black made white', 'red')
    True
    >>> find_word('The red and the black made white', 'black')
    True
    >>> find_word('The red and the black made white', 'white')
    False
    """
    # split the sentence into a list of words
    # use the find function to search for the word in the list
    # return the result
    pass


def count_word(sentence: str, word: str) -> int:
    """ Input is a string of one or more words and a word to search for.
    Return the number of times the word appears in the string.
    >>> count_word('The red and the black made white', 'red')
    1
    >>> count_word('The red and the black made white', 'the')
    2
    >>> count_word