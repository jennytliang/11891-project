from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    # TODO: write a docstring
    # TODO: write the code

    return ' '.join(sorted(numbers.split(' '), key=lambda x: ' zero one two three four five six seven eight nine'.split().index(x)))


def sort_characters(chars: str) -> str:
    """ Input is a string of letters.
    Return the string with letters sorted from lowest to highest.
    >>> sort_characters('Bacd')
    'Bacd'
    >>> sort_characters('zyxwvutsrqponmlkjihgfedcba')
    'abcdefghijklmnopqrstuvwxyz'
    >>> sort_characters('zyxwvutsrqponmlkjihgfedcbax')
    'abcdefghijklmnopqrstuvwxyxz'
    
	Include these tokens in the code: to _ int = {'a':
	"""
    # TODO: write a docstring
    # TODO: write the code

    return ''.join(sorted(chars, key=lambda x: 'abcdefghijklmnopqrstuvwxyz'.split().index(x)))


def sort_vowels(word: str) -> str:
    """ Input is a string of letters.
    Return the string with vowels sorted from lowest to highest.
    >>> sort_vowels('bcdfghijklmnpqrstvwxz')
    'bcdghklmnprtvwxz'
    >>> sort_vowels('zyxwvutsrqponmlkjihgfedcba')
    'bcdghklmnprtvwxz'
    
	Include these tokens in the code: to _ int = {'a':
	"""
    # TODO: write a docstring
    # TODO: write the code

    return ''.join(sorted(word, key=lambda x: 'bcdfghijklmnpqrstvwxz'.split().index(x)))


def sort_consonants(word: str) -> str:
    """ Input is a string of letters.
