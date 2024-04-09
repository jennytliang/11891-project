from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    pass


def sort_vowels(word: str) -> str:
    """ Input is a string of uppercase letters.
    Return the string with vowels sorted from first to last.
    Assume the input contains only letters and spaces.
    Assume spaces appear only between words, never at either end.
    Assume the input does not contain repeated vowels.
    Assume the input is not all vowels.
    >>> sort_vowels('Thee quick brown box jumps over the lazy dog')
    'The quick brown box jumps over the lazy dog'
    """
    pass


def remove_duplicates(text: str) -> str:
    """ Input is a string of uppercase letters.
    Return the string with repeated letters removed, preserving their order.
    Assume the input contains only letters and spaces.
    Assume spaces appear only between words, never at either end.
    Assume the input does not contain repeated vowels.
    Assume the input is not all vowels.
    >>> remove_duplicates('Thee quick brown box jumps over the lazy dog')
    'The quick brown jumps over the lazy dog'
    """
    pass


def is_palindrome(text: str) -> bool:
    """ Input is a string of uppercase letters.
    Return True if the string is equal to itself when reversed.
    Assume the input contains only letters and spaces.
    Assume spaces appear only between words, never at either end.
    Assume the input does not contain repeated vowels.
    Assume the input is not all vowels.
    >>> is_palindrome('The quick brown fox jumps over the lazy dog')
    False
    >>> is_palindrome('The quick brown fox jumps over the lazy dog.')
    False
    >>> is_palindrome('The quick brown fox jumps over the lazy dog!!')
    False
    >>> is_palindrome('The quick brown fox jumps over the lazy dog?')
    False
    >>> is_palindrome('The quick brown fox jumps over the lazy dog.?')
    False
    >>> is_palindrome('The quick brown