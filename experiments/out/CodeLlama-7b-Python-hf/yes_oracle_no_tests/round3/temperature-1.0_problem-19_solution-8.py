from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # Convert string to list
    lst = [int(x) for x in numbers.split()]
    # Sort list
    lst.sort()
    # Join list to string
    return ' '.join(str(x) for x in lst)


def sort_words(words: str) -> str:
    """ Input is a string of words, separated by spaces.
    Return the string with words sorted from shortest to longest
    >>> sort_words('cat dog elephant')
    'cat dog elephant'
    """
    # Convert string to list
    lst = words.split()
    # Sort list
    lst.sort(key=len)
    # Join list to string
    return ' '.join(lst)


def sort_sentence(sentence: str) -> str:
    """ Input is a string containing a single sentence.
    Return the string with the words sorted from longest to shortest
    >>> sort_sentence('python is cool')
    'cool is python'
    """
    # Convert string to list
    lst = sentence.split()
    # Sort list
    lst.sort(key=len, reverse=True)
    # Join list to string
    return ' '.join(lst)


def sort_capital(sentence: str) -> str:
    """ Input is a string containing a single sentence.
    Return the string with all words capitalized, and sorted from longest to shortest"""
    # Convert string to list
    lst = sentence.split()
    # Sort list
    lst.sort(key=len, reverse=True)
    # Join list to string
    return ' '.join(x.capitalize() for x in lst)


def sort_vowels(sentence: str) -> str:
    """ Input is a string containing a single sentence.
    Return the string with the vowels stripped out, and sorted from a to z"""
    # Convert string to list
    lst = sentence.split()
    # Sort list
    lst.sort()
    # Join list to string
    return ' '.join(x.translate(str.maketr